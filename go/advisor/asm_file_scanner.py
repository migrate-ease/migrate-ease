"""
Copyright 2020-2023 Alibaba Inc.

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
import os
import re
import time

from common.arch_strings import AARCH64_ARCHS
from common.checkpoint import Checkpoint, init_checkpoints
from common.continuation_parser import ContinuationParser
from common.find_port import find_matching_line_num
from common.report_factory import ReportOutputFormat

from .asm_issue import AsmIssue
from .go_scanner import GoScanner
from .golang_asm_strings import GOLANG_ASM_AARCH64, NON_GOLANG_ASM_AARCH64


class AsmFileScanner(GoScanner):
    """
    Scanner that scans .s source files for potential porting issues
    """

    PY_SOURCE_EXTENSIONS = ['.s']

    AARCH64_NAME_RE = re.compile(r'.*(%s).*' % '|'.join([(r'%s' % x) for x in GOLANG_ASM_AARCH64]))
    NON_AARCH64_NAME_RE = re.compile(r'.*(%s).*' % '|'.join([(r'%s' % x) for x in NON_GOLANG_ASM_AARCH64]))

    AARCH64_INCOMPATIBLE_PLAN9_GOLANG_INTRINSICS = []

    def __init__(self, output_format, arch, march):
        self.output_format = output_format
        self.arch = arch
        self.march = march

        self.with_highlights = bool(
            output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)
        self.load_checkpoints()

    def load_checkpoints(self):
        super().load_checkpoints()

        start_time = time.time()

        self.AARCH64_INCOMPATIBLE_PLAN9_GOLANG_INTRINSICS = init_checkpoints(
            self.checkpoints_content['PLAN9_GOLANG_X86']
        )

        end_time = time.time()

        print('[Go] Initialization of checkpoints took %f seconds.' % (end_time - start_time))

    def accepts_file(self, filename):

        _, ext = os.path.splitext(filename)
        return ext.lower() in self.__class__.PY_SOURCE_EXTENSIONS

    def scan_file_object(self, filename, file_obj, report):

        _lines = file_obj.readlines()
        _, ext = os.path.splitext(filename)

        if ext.lower() in self.__class__.PY_SOURCE_EXTENSIONS:
            self.FILE_SUMMARY[self.S]['count'] += 1
            self.FILE_SUMMARY[self.S]['loc'] += len(_lines)

        match_arch = ''
        match_non_arch = ''

        continuation_parser = ContinuationParser()

        issues = []  # type: List[Issue]
        lines = {}

        if self.arch in AARCH64_ARCHS:

            match_arch = self.__class__.AARCH64_NAME_RE.search(os.path.basename(filename))
            match_non_arch = self.__class__.NON_AARCH64_NAME_RE.search(os.path.basename(filename))
            PLAN9_ASSEMBLY_CHECKPOINTS = self.AARCH64_INCOMPATIBLE_PLAN9_GOLANG_INTRINSICS

        if match_arch and not match_non_arch:

            issues = []

        elif not match_arch and match_non_arch:

            lines[0] = "File: " + filename + " is not supported on arch: " + self.arch

            issues.append(AsmIssue(filename=filename,
                                   arch=self.arch,
                                   lineno=0,
                                   checkpoint=None,
                                   description=lines[0]))

        else:

            for lineno, line in enumerate(_lines, 1):
                lines[lineno] = line

            match = ''

            for lineno in lines.keys():

                line = lines[lineno]

                line = continuation_parser.parse_line(line)
                if not line:
                    continue

                c: Checkpoint
                for c in PLAN9_ASSEMBLY_CHECKPOINTS:
                    match = c.pattern_compiled.search(line)

                    if match:
                        issues.append(AsmIssue(filename=filename,
                                               lineno=find_matching_line_num(lines, lineno, c.pattern),
                                               intrinsic=match.string.strip(),
                                               arch=self.arch,
                                               checkpoint=c.pattern,
                                               description='' if not c.help else '\n' + c.help))

        #  to extract code snippets
        for issue in issues:
            issue.set_code_snippet(issue.get_code_snippets(lines, with_highlights=self.with_highlights))
            report.add_issue(issue)
