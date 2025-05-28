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
from typing import List

from common.arch_strings import AARCH64_ARCHS
from common.checkpoint import Checkpoint, init_checkpoints
from common.continuation_parser import ContinuationParser
from common.naive_comment_parser import NaiveCommentParser
from common.report_factory import ReportOutputFormat
from common.issue import Issue

from cpp.advisor.clang_source_scanner import ClangSourceScanner

from .python_inline_asm_issue import PythonInlineAsmIssue
from .python_intrinsic_issue import PythonIntrinsicIssue
from .python_package_issue import PythonPakageIssue
from .python_cpp_std_issue import PythonCPPStdCodesIssue
from .python_scanner import PythonScanner


class PythonFileScanner(PythonScanner):

    """
    Scanner that scans .py source files for potential porting issues
    """

    AARCH64_INCOMPATIBLE_EXTENSION_PACKAGES = []
    PACKAGE_CHECKPOINTS = []
    PY_SOURCE_EXTENSIONS = ['.py']
    # from cffi import FFI
    # import cffi
    LINK_CFFI_RE = re.compile(r'^\s*(from\s+cffi\s+import\s+FFI|import\s+cffi)\s*$')

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

        if self.arch in AARCH64_ARCHS:
            self.PACKAGE_CHECKPOINTS = self.AARCH64_INCOMPATIBLE_EXTENSION_PACKAGES
        else:
            self.PACKAGE_CHECKPOINTS = None

        continuation_parser = ContinuationParser()
        comment_parser = NaiveCommentParser()
        cpp_scanner = ClangSourceScanner(self.output_format, self.arch, self.march)

        issues: List[Issue] = []
        lines = {lineno: line for lineno, line in enumerate(_lines, 1)}
        match_cffi=None

        for lineno in lines.keys():
            line = lines[lineno]
            if line.strip() == "" or line.lstrip().startswith('#'):
                continue
            line = continuation_parser.parse_line(line)
            if not line:
                continue

            if not match_cffi:
                match_cffi = self.__class__.LINK_CFFI_RE.search(line.strip())
            start_line = None
            if match_cffi:
                # cffi.set_source(
                #  """
                #  Embedding C code in the cffi module
                #  """)
                #
                # Identify and scan the embedded C code.
                if 'ffi.set_source' in line:
                    while lineno <= len(lines):
                        line = lines[lineno]
                        if '\"\"\"' in line:
                            if not start_line:
                                start_line = lineno+1
                                lineno = start_line
                                continue
                            else:
                                break
                        if line.strip() == "":
                            lineno += 1
                            continue
                        line = continuation_parser.parse_line(line)
                        if not line:
                            lineno += 1
                            continue
                        is_comment = comment_parser.parse_line(line)
                        if is_comment:
                            lineno += 1
                            continue
                        line = continuation_parser.join_line(line, lineno)
                        if not line:
                            lineno += 1
                            continue
                        next_lineno = 1
                        next_lineno = cpp_scanner.check_clang(lines, line, lineno, continuation_parser.joined_lineno, filename,
                                                      PythonInlineAsmIssue, PythonIntrinsicIssue, PythonCPPStdCodesIssue,
                                                      issues)
                        if next_lineno != 1:
                            # check_clang already parses multiple lines of code, so there's no need to repeat the parsing logic here.
                            lineno = next_lineno+1
                        else:
                            lineno += 1

                        # Reset the joined line number.
                        continuation_parser.joined_lineno = -1

            c: Checkpoint
            for c in self.PACKAGE_CHECKPOINTS:
                match = c.pattern_compiled.search(line)
                if match:
                    issues.append(PythonPakageIssue(filename,
                                                    lineno=lineno,
                                                    checkpoint=c.pattern,
                                                    description='' if not c.help else '\n' + c.help))
                    break


        # to extract code snippets
        for issue in issues:
            issue.set_code_snippet(issue.get_code_snippets(lines, with_highlights=self.with_highlights))
            report.add_issue(issue)

    def finalize_report(self, report):
        pass
