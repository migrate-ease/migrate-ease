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

from common.arch_strings import AARCH64_ARCHS, NON_AARCH64_ARCHS
from common.continuation_parser import ContinuationParser
from common.naive_comment_parser import NaiveCommentParser
from common.report_factory import ReportOutputFormat
from common.checkpoint import init_checkpoints

from .configuration_info_issue import ConfigurationInfoIssue
from .docker_scanner import DockerScanner
from .image_issue import ImageIssue
from .naive_dockerfile import NaiveDockerfile, PreprocessorDirective
from .plugin_issue import PluginIssue


class DockerfileScanner(DockerScanner):
    """
    Scanner that scans dockerfiles for potential porting issues
    """

    DOCKERFILE_SOURCE = ['Dockerfile', 'dockerfile']

    NON_AARCH64_RE = re.compile(r'.*(%s).*' % '|'.join([(r'%s' % x) for x in NON_AARCH64_ARCHS]))

    AARCH64_INCOMPATIBLE_EXTENSION_PACKAGES = []

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

        self.AARCH64_INCOMPATIBLE_EXTENSION_PACKAGES = init_checkpoints(
            self.checkpoints_content['X86_PYTHON_EXTENSION_PACKAGES'],
            self.checkpoints_content["AARCH64_PYTHON_EXTENSION_PACKAGES"] +
            self.checkpoints_content["COMMON_AARCH64_AND_X86_PYTHON_EXTENSION_PACKAGES"]
        )

        # please remember to remove lines for profiling after optimizing :)
        end_time = time.time()

        print('[Docker] Initialization of checkpoints took %f seconds.' % (end_time - start_time))

    def accepts_file(self, filename):

        ext = os.path.basename(filename)
        return ext.lower() in self.__class__.DOCKERFILE_SOURCE

    def scan_file_object(self, filename, file_obj, report):

        _lines = file_obj.readlines()
        ext = os.path.basename(filename)

        if ext.lower() in self.__class__.DOCKERFILE_SOURCE:
            self.FILE_SUMMARY[self.DOCKERFILE]['count'] += 1
            self.FILE_SUMMARY[self.DOCKERFILE]['loc'] += len(_lines)

        continuation_parser = ContinuationParser()
        naive_dockerfile = NaiveDockerfile(arch=self.arch, march=self.march)
        comment_parser = NaiveCommentParser()

        if self.arch in AARCH64_ARCHS:

            PACKAGE_CHECKPOINTS = self.AARCH64_INCOMPATIBLE_EXTENSION_PACKAGES
            ARCH_RE = self.NON_AARCH64_RE

        else:

            PACKAGE_CHECKPOINTS = None
            ARCH_RE = None

        issues = []  # type: List[Issue]
        lines = {}
        match_cffi = ''

        for lineno, line in enumerate(_lines, 1):
            lines[lineno] = line

        for lineno in lines.keys():

            line = lines[lineno]

            line = continuation_parser.parse_line(line)
            if not line:
                continue

            is_comment = comment_parser.parse_line(line)
            if is_comment:
                continue

            result = naive_dockerfile.parse_line(line)  # type: PreprocessorDirective

            # FROM
            if result.directive_type == PreprocessorDirective.TYPE_FROM:

                parts = line.strip(result.directive_type)

                issues.append(ImageIssue(filename,
                                         lineno,
                                         arch=self.arch,
                                         image=parts,
                                         checkpoint=None))

            # RUN/CMD/ENTRYPOINT
            elif result.directive_type in PreprocessorDirective.TYPE_EXEC_COMMAND:

                # python package check
                for c in PACKAGE_CHECKPOINTS:

                    match = c.pattern_compiled.search(line)
                    if match:
                        issues.append(PluginIssue(filename,
                                                  lineno,
                                                  arch=self.arch,
                                                  plugin=c.pattern,
                                                  checkpoint=c.pattern,
                                                  description='' if not c.help else '\n' + c.help))

            # ENV/ARG/LABEL
            elif result.directive_type in PreprocessorDirective.TYPE_OTHER_COMMAND:

                match = ARCH_RE.search(line)
                if match:
                    issues.append(ConfigurationInfoIssue(filename,
                                                         lineno,
                                                         arch=self.arch,
                                                         checkpoint=line,
                                                         description=None))

        #  to extract code snippets
        for issue in issues:
            issue.set_code_snippet(issue.get_code_snippets(lines, with_highlights=self.with_highlights))
            report.add_issue(issue)
