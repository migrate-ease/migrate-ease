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

from common.continuation_parser import ContinuationParser
from common.naive_comment_parser import NaiveCommentParser
from common.report_factory import ReportOutputFormat
from common.issue import Issue

from cpp.advisor.clang_source_scanner import ClangSourceScanner

from .go_scanner import GoScanner
from .golang_inline_asm_issue import GolangInlineAsmIssue
from .golang_intrinsic_issue import GolangIntrinsicIssue
from .golang_cpp_std_issue import GolangCPPStdCodesIssue


class GolangFileScanner(GoScanner):

    """
    Scanner that scans .go source files for potential porting issues
    """

    GO_SOURCE_EXTENSIONS = ['.go']

    #In Go, import "C" is the standard way to import C code and cannot be replaced by other forms.
    C_IMPORT_RE = re.compile(r'^import\s+"C"$')

    def __init__(self, output_format, arch, march):
        self.output_format = output_format
        self.arch = arch
        self.march = march

        self.with_highlights = bool(
            output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)
        self.load_checkpoints()

    def accepts_file(self, filename):

        _, ext = os.path.splitext(filename)
        return ext.lower() in self.__class__.GO_SOURCE_EXTENSIONS

    def scan_file_object(self, filename, file_obj, report):

        _lines = file_obj.readlines()
        _, ext = os.path.splitext(filename)

        if ext.lower() in self.__class__.GO_SOURCE_EXTENSIONS:
            self.FILE_SUMMARY[self.GO]['count'] += 1
            self.FILE_SUMMARY[self.GO]['loc'] += len(_lines)

        match_c = ''
        continuation_parser = ContinuationParser()
        comment_parser = NaiveCommentParser()
        cpp_scanner = ClangSourceScanner(self.output_format, self.arch, self.march)
        issues: List[Issue] = []
        lines = {lineno: line for lineno, line in enumerate(_lines, 1)}

        for lineno in range (1, len(lines.keys())+1):
            line = lines[lineno]
            match_c = self.__class__.C_IMPORT_RE.search(line)
            # Check whether C code blocks are referenced via cgo in the Go source.
            if not match_c:
                continue

            # The C code block is enclosed in /* ... */.
            # By identifying the start and end lines of this block, we can prevent it from
            # being mistakenly parsed as a regular comment later.
            for lineno_s in range(1, lineno):
                if lines[lineno_s].strip() == "/*":
                    break
            for lineno_e in range(lineno, lineno_s, -1):
                if lines[lineno_e].strip() == "*/":
                    break

            # Parse the C code block enclosed in /* ... */ before import "C".
            lineno_c = lineno_s+1
            while lineno_c < lineno_e:
                line = lines[lineno_c]
                if line.strip() == "":
                    lineno_c += 1
                    continue
                line = continuation_parser.parse_line(line)
                if not line:
                    lineno_c += 1
                    continue
                is_comment = comment_parser.parse_line(line)
                if is_comment:
                    lineno_c += 1
                    continue
                line = continuation_parser.join_line(line, lineno_c)
                if not line:
                    lineno_c += 1
                    continue
                next_lineno = 1
                next_lineno = cpp_scanner.check_clang(lines, line, lineno_c, continuation_parser.joined_lineno, filename,
                                                      GolangInlineAsmIssue, GolangIntrinsicIssue, GolangCPPStdCodesIssue,
                                                      issues)
                if next_lineno != 1:
                    # check_clang already parses multiple lines of code, so there's no need to repeat the parsing logic here.
                    lineno_c = next_lineno+1
                else:
                    lineno_c += 1

                # Reset the joined line number.
                continuation_parser.joined_lineno = -1

            #  to extract code snippets
            for issue in issues:
                issue.set_code_snippet(issue.get_code_snippets(lines, with_highlights=self.with_highlights))
                report.add_issue(issue)
            break


    def finalize_report(self, report):
        pass
