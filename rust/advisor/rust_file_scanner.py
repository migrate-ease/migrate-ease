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

from common.arch_strings import *
from common.continuation_parser import ContinuationParser
from common.find_port import find_matching_line_num
from common.naive_comment_parser import NaiveCommentParser
from common.report_factory import ReportOutputFormat
from .checkpoints import AARCH64_INCOMPATIBLE_INTRINSICS, AARCH64_INLINE_ASSEMBLY_CHECKPOINTS
from .rust_inline_asm_issue import RustInlineAsmIssue
from .rust_intrinsic_issue import RustIntrinsicIssue
from .rust_scanner import RustScanner


class RustFileScanner(RustScanner):
    """
    Scanner that scans .rs source files for potential porting issues
    """

    RS_SOURCE_EXTENSIONS = ['.rs']

    def __init__(self, output_format, arch, march):
        self.output_format = output_format
        self.arch = arch
        self.march = march

        self.with_highlights = bool(
            output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)

    def accepts_file(self, filename):

        _, ext = os.path.splitext(filename)
        return ext.lower() in self.__class__.RS_SOURCE_EXTENSIONS

    def scan_file_object(self, filename, file_obj, report):

        _lines = file_obj.readlines()
        _, ext = os.path.splitext(filename)

        if ext.lower() in self.__class__.RS_SOURCE_EXTENSIONS:
            self.FILE_SUMMARY[self.RUST]['count'] += 1
            self.FILE_SUMMARY[self.RUST]['loc'] += len(_lines)

        continuation_parser = ContinuationParser()
        comment_parser = NaiveCommentParser()

        if self.arch in AARCH64_ARCHS:

            ARCH_INCOMPATIBLE_INTRINSICS = AARCH64_INCOMPATIBLE_INTRINSICS
            ASSEMBLY_CHECKPOINTS = AARCH64_INLINE_ASSEMBLY_CHECKPOINTS

        else:

            ARCH_INCOMPATIBLE_INTRINSICS = None
            ASSEMBLY_CHECKPOINTS = None

        issues = []  # type: List[Issue]
        lines = {}

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

            #  inline assembly check
            for c in ASSEMBLY_CHECKPOINTS:
                #  NOTE: inline asm can expand no more than two lines
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
                    issues.append(RustInlineAsmIssue(filename,
                                                     lineno=lineno,
                                                     checkpoint=c.pattern,
                                                     description='' if not c.help else '\n' + c.help))
                    break

            #  intrinsics check
            for c in ARCH_INCOMPATIBLE_INTRINSICS:

                match = c.pattern_compiled.search(line)

                if match:
                    issues.append(RustIntrinsicIssue(filename,
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
