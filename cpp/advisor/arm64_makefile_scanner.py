"""
Copyright 2020-2023 Alibaba Inc.
Copyright 2017-2020 Arm Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import re
import time

from common.arch_strings import AARCH64_ARCHS, NON_AARCH64_ARCHS
from common.continuation_parser import ContinuationParser
from common.report_factory import ReportOutputFormat
from common.checkpoint import init_checkpoints
from .arch_specific_library_issue import ArchSpecificLibraryIssue
from .arch_specific_libs import ARM64_ARCH_SPECIFIC_LIBS
from .build_command_issue import BuildCommandIssue
from .define_other_arch_issue import DefineOtherArchIssue
from .host_cpu_detection_issue import HostCpuDetectionIssue
from .makefile_scanner import MakefileScanner
from .old_crt_issue import OldCrtIssue


class Arm64MakefileScanner(MakefileScanner):

    """
    Scanner that scans Makefiles.
    """
    AARCH64_COMPILER_OPTION_CHECKPOINTS = []

    ARCH_SPECIFIC_LIBS_RE = re.compile(r'(%s)' % '|'.join([(r'%s\b' % x) for x in ARM64_ARCH_SPECIFIC_LIBS]))

    #  ('!IF "$(CPU)" == "otherarch"')
    #  ('!IF "$(VSCMD_ARG_TGT_ARCH)" == "aarch64"')
    AARCH64_CPU_LINE_RE = re.compile(r'\$\(VSCMD_ARG_TGT_ARCH\).*(%s)' % '|'.join(AARCH64_ARCHS))

    OTHER_ARCH_CPU_LINE_RE = re.compile(r'\$\((?:CPU|PROCESSOR_ARCHITECTURE)\).*(%s)' % '|'.join(NON_AARCH64_ARCHS))

    D_AARCH64_RE = re.compile(r'[-/]D(%s)' %
                              '|'.join(AARCH64_ARCHS +
                                       [x.upper() for x in AARCH64_ARCHS] +
                                       [('_%s_' % x) for x in AARCH64_ARCHS] +
                                       [('_%s_' % x.upper()) for x in AARCH64_ARCHS] +
                                       [('__%s__' % x) for x in AARCH64_ARCHS] +
                                       [('__%s__' % x.upper()) for x in AARCH64_ARCHS]))

    D_OTHER_ARCH_RE = re.compile(r'[-/]D(%s)' %
                                 '|'.join(NON_AARCH64_ARCHS +
                                          [x.upper() for x in NON_AARCH64_ARCHS] +
                                          [('_%s_' % x) for x in NON_AARCH64_ARCHS] +
                                          [('_%s_' % x.upper()) for x in NON_AARCH64_ARCHS] +
                                          [('__%s__' % x) for x in NON_AARCH64_ARCHS] +
                                          [('__%s__' % x.upper()) for x in NON_AARCH64_ARCHS]))

    def __init__(self, output_format, march):
        self.output_format = output_format
        self.march = march
        self.highlight_code_snippet = bool(self.output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)
        self.load_checkpoints()

    def load_checkpoints(self):
        super().load_checkpoints()

        start_time = time.time()

        self.AARCH64_COMPILER_OPTION_CHECKPOINTS = init_checkpoints(
            self.checkpoints_content["AARCH64_COMPILER_OPTION_CHECKPOINTS"]
            )

        # please remember to remove lines for profiling after optimizing :)
        end_time = time.time()

        print('[C/C++] Initialization of checkpoints took %f seconds.' % (end_time - start_time))

    def scan_file_object(self, filename, file_obj, report):

        _lines = file_obj.readlines()
        self.FILE_SUMMARY[self.MAKEFILE]['count'] += 1
        self.FILE_SUMMARY[self.MAKEFILE]['loc'] += len(_lines)

        continuation_parser = ContinuationParser()
        targets = set()
        commands = set()
        assignments = dict()

        issues = []
        lines = {}
        for lineno, line in enumerate(_lines, 1):

            lines[lineno] = line

            line = continuation_parser.parse_line(line)

            if not line:
                continue

            #  check of target processor architecture specifc libs
            match = self.__class__.ARCH_SPECIFIC_LIBS_RE.search(line)
            if match:
                lib_name = match.group(1)
                issues.append(ArchSpecificLibraryIssue(filename,
                                                       lineno,
                                                       lib_name=lib_name,
                                                       march=self.march))

            #  check of old C Runtime libs, if universal CRT found
            #  then it will not be seen as an issue, be note that
            #  such check performs only once per file.
            match = self.__class__.OLD_CRT_RE.search(line)
            if match:
                old_crt_lib_name = match.group(0)
                if old_crt_lib_name:
                    issues.append(OldCrtIssue(filename,
                                              lineno,
                                              old_crt_lib_name))

            #  check of other CPU archs related lines
            match = self.__class__.OTHER_ARCH_CPU_LINE_RE.search(line)
            if match:
                issues.append(HostCpuDetectionIssue(filename,
                                                    lineno,
                                                    line))

            #  check of target processor architecture specific macros
            match = self.__class__.D_OTHER_ARCH_RE.search(line)
            if match:
                d_other_arch = match.group(0)
                if d_other_arch:
                    issues.append(DefineOtherArchIssue(filename,
                                                       lineno,
                                                       d_other_arch))

            #  check of makefile assignment
            match = self.__class__.ASSIGNMENT_RE.search(line)
            if match:
                assignments['$(%s)' % match.group(1)] = match.group(2)

            #  check of makefile target
            match = self.__class__.TARGET_RE.search(line)
            if match:
                target = match.group(1)
                if target.startswith('./') or target.startswith('.\\'):
                    target = target[2:]
                targets.add(target)

                build_commands = targets.intersection(commands)

                if target in build_commands:
                    if target in assignments:
                        target = assignments[target]

                    issues.append(BuildCommandIssue(filename,
                                                    lineno,
                                                    target=target))
            #  check of makefile command
            match = self.__class__.COMMAND_RE.search(line)
            if match:
                command = match.group(1)
                if not command:
                    command = match.group(2)
                if command.startswith('./') or command.startswith('.\\'):
                    command = command[2:]
                commands.add(command)

                build_commands = targets.intersection(commands)

                if command in build_commands:
                    if command in assignments:
                        command = assignments[command]

                    issues.append(BuildCommandIssue(filename,
                                                    lineno,
                                                    target=command))

            #  other check points
            for c in self.AARCH64_COMPILER_OPTION_CHECKPOINTS:

                match = c.pattern_compiled.search(line)

                if match:
                    issues.append(BuildCommandIssue(filename,
                                                    lineno,
                                                    checkpoint=c.pattern,
                                                    description='' if not c.help else '\n' + c.help))
                    break

        for issue in issues:
            issue.set_code_snippet(issue.get_code_snippets(lines, with_highlights=self.highlight_code_snippet))
            report.add_issue(issue)
