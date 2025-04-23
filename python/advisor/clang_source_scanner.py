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
from common.naive_comment_parser import NaiveCommentParser
from common.report_factory import ReportOutputFormat

from .python_inline_asm_issue import PythonInlineAsmIssue
from .python_intrinsic_issue import PythonIntrinsicIssue
from .python_package_issue import PythonPakageIssue
from .python_scanner import PythonScanner


class ClangSourceScanner(PythonScanner):

    """
    Scanner that scans .py source files for potential porting issues
    """

    AARCH64_INCOMPATIBLE_EXTENSION_PACKAGES = []
    AARCH64_INCOMPATIBLE_INTRINSICS = []
    AARCH64_INLINE_ASSEMBLY_CHECKPOINTS = []

    PY_SOURCE_EXTENSIONS = ['.py']

    LINK_CFFI_RE = re.compile(r'.*(cffi).*')

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
        self.AARCH64_INCOMPATIBLE_INTRINSICS = init_checkpoints(
            self.checkpoints_content['X86_INTRINSICS'] + self.checkpoints_content['OTHER_ARCH_INTRINSICS'] + self.checkpoints_content['INCOMPATIBLE_UCRT_INTRINSICS'],
            self.checkpoints_content["COMMON_INTRINSICS"] + self.checkpoints_content["AARCH64_INTRINSICS"]
        )
        self.AARCH64_INLINE_ASSEMBLY_CHECKPOINTS = init_checkpoints(
            self.checkpoints_content["AARCH64_INLINE_ASSEMBLY_CHECKPOINTS"]
        )

        end_time = time.time()

        print('[Python] Initialization of checkpoints took %f seconds.' % (end_time - start_time))

    def accepts_file(self, filename):

        _, ext = os.path.splitext(filename)
        return ext.lower() in self.__class__.PY_SOURCE_EXTENSIONS

    def scan_file_object(self, filename, file_obj, report):

        _lines = file_obj.readlines()
        _, ext = os.path.splitext(filename)

        if ext.lower() in self.__class__.PY_SOURCE_EXTENSIONS:

            self.FILE_SUMMARY[self.PY]['count'] += 1
            self.FILE_SUMMARY[self.PY]['loc'] += len(_lines)

        continuation_parser = ContinuationParser()
        comment_parser = NaiveCommentParser()

        if self.arch in AARCH64_ARCHS:

            ARCH_INCOMPATIBLE_INTRINSICS = self.AARCH64_INCOMPATIBLE_INTRINSICS
            ASSEMBLY_CHECKPOINTS = self.AARCH64_INLINE_ASSEMBLY_CHECKPOINTS
            PACKAGE_CHECKPOINTS = self.AARCH64_INCOMPATIBLE_EXTENSION_PACKAGES

        else:

            ARCH_INCOMPATIBLE_INTRINSICS = None
            ASSEMBLY_CHECKPOINTS = None
            PACKAGE_CHECKPOINTS = None

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

            c: Checkpoint
            for c in PACKAGE_CHECKPOINTS:

                match = c.pattern_compiled.search(line)

                if match:
                    issues.append(PythonPakageIssue(filename,
                                                    lineno=lineno,
                                                    checkpoint=c.pattern,
                                                    description='' if not c.help else '\n' + c.help))

            if not match_cffi:

                match_cffi = self.__class__.LINK_CFFI_RE.search(line)

            if match_cffi:

                c: Checkpoint
                for c in ASSEMBLY_CHECKPOINTS:
                    #  NOTE: inline asm can expand no more that two lines
                    if (lineno + 4) <= len(lines.keys()):
                        multiline = "".join([lines[_] for _ in range(lineno, lineno + 5)])
                        match = c.pattern_compiled.search(multiline)
                    elif (lineno + 3) <= len(lines.keys()):
                        multiline = "".join([lines[_] for _ in range(lineno, lineno + 4)])
                        match = c.pattern_compiled.search(multiline)
                    elif (lineno + 2) <= len(lines.keys()):
                        multiline = "".join([lines[_] for _ in range(lineno, lineno + 3)])
                        match = c.pattern_compiled.search(multiline)
                    elif (lineno + 1) <= len(lines.keys()):
                        multiline = "".join([lines[_] for _ in range(lineno, lineno + 2)])
                        match = c.pattern_compiled.search(multiline)
                    else:
                        match = c.pattern_compiled.search(line)

                    if match:
                        issues.append(PythonInlineAsmIssue(filename,
                                                           lineno=lineno,
                                                           checkpoint=c.pattern,
                                                           description='' if not c.help else '\n' + c.help))
                        break

                #  intrinsics check
                for c in ARCH_INCOMPATIBLE_INTRINSICS:

                    match = c.pattern_compiled.search(line)

                    if match:
                        issues.append(PythonIntrinsicIssue(filename,
                                                           lineno=find_matching_line_num(lines, lineno, c.pattern),
                                                           arch=self.arch,
                                                           intrinsic=match.string.strip(),
                                                           checkpoint=c.pattern,
                                                           description='' if not c.help else '\n' + c.help))
                        break

        #  to extract code snippets
        for issue in issues:
            issue.set_code_snippet(issue.get_code_snippets(lines, with_highlights=self.with_highlights))
            report.add_issue(issue)

    def finalize_report(self, report):
        pass
