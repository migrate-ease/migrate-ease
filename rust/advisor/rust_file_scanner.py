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

from common.arch_strings import *
from common.continuation_parser import ContinuationParser
from common.find_port import find_matching_line_num
from common.naive_comment_parser import NaiveCommentParser
from common.report_factory import ReportOutputFormat
from common.checkpoint import init_checkpoints
from common.issue import Issue

from .rust_inline_asm_issue import RustInlineAsmIssue
from .rust_intrinsic_issue import RustIntrinsicIssue
from .rust_scanner import RustScanner


class RustFileScanner(RustScanner):
    """
    Scanner that scans .rs source files for potential porting issues
    """

    RS_SOURCE_EXTENSIONS = ['.rs']
    inlineAsm_pattern = re.compile(r'(?mis)\A\s*(global_asm!|asm!|llvm_asm!)')

    AARCH64_INCOMPATIBLE_INTRINSICS = []
    AARCH64_INLINE_ASSEMBLY_CHECKPOINTS = []
    ARCH_INCOMPATIBLE_INTRINSICS = []
    ASSEMBLY_CHECKPOINTS = []

    def __init__(self, output_format, march):
        self.output_format = output_format
        self.march = march

        self.with_highlights = bool(
            self.output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)
        self.load_checkpoints()

    def load_checkpoints(self):
        super().load_checkpoints()

        start_time = time.time()

        self.AARCH64_INCOMPATIBLE_INTRINSICS = init_checkpoints(
            self.checkpoints_content['X86_INTRINSICS'] + self.checkpoints_content['OTHER_ARCH_INTRINSICS'] ,
            self.checkpoints_content["COMMON_INTRINSICS"] + self.checkpoints_content["AARCH64_INTRINSICS"]
        )

        self.AARCH64_INLINE_ASSEMBLY_CHECKPOINTS = init_checkpoints(
            self.checkpoints_content["AARCH64_INLINE_ASSEMBLY_CHECKPOINTS"]
        )

        end_time = time.time()

        print('[Rust] Initialization of checkpoints took %f seconds.' % (end_time - start_time))

    def accepts_file(self, filename):

        _, ext = os.path.splitext(filename)
        return ext.lower() in self.__class__.RS_SOURCE_EXTENSIONS

    def scan_file_object(self, filename, file_obj, report):

        _lines = file_obj.readlines()
        _, ext = os.path.splitext(filename)

        if ext.lower() in self.__class__.RS_SOURCE_EXTENSIONS:
            self.FILE_SUMMARY[self.RUST]['count'] += 1
            self.FILE_SUMMARY[self.RUST]['loc'] += len(_lines)

        if self.march in SUPPORTED_MARCH:
            self.ARCH_INCOMPATIBLE_INTRINSICS = self.AARCH64_INCOMPATIBLE_INTRINSICS
            self.ASSEMBLY_CHECKPOINTS = self.AARCH64_INLINE_ASSEMBLY_CHECKPOINTS
        else:
            raise RuntimeError('no scanner available for target processor architecture %s.' % self.march)

        continuation_parser = ContinuationParser()
        comment_parser = NaiveCommentParser()
        issues: List[Issue] = []
        lines = {lineno: line for lineno, line in enumerate(_lines, 1)}

        for lineno in range(1, len(lines.keys())+1):
            line = lines[lineno]
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
            next_lineno = self.check_issues(lines, line, lineno, continuation_parser.joined_lineno, filename, issues)
            if next_lineno != 1:
                # check_clang already parses multiple lines of code, so there's no need to repeat the parsing logic here.
                lineno = next_lineno+1
            else:
                lineno += 1

            # Reset the joined line number.
            continuation_parser.joined_lineno = -1

        #  to extract code snippets
        for issue in issues:
            issue.set_code_snippet(issue.get_code_snippets(lines, with_highlights=self.with_highlights))
            report.add_issue(issue)

    def check_issues(self,
                     # context
                     lines, line, lineno, joined_lineno, filename,
                     # results
                     issues: List[Issue]):

        continuation_parser = ContinuationParser()
        # inline assemly check.
        # Check for inline asm (e.g., 'asm!(...)' or 'global_asm!(...)')
        match = self.inlineAsm_pattern.match(line.strip())
        if match:
            if lineno < len(lines) and lines[lineno+1].strip().startswith('('):
                # The inline assembly function is written across multiple lines.
                lineno = lineno+1
                join_line = continuation_parser.join_line(lines[lineno])
                while continuation_parser.joined_line != None:
                    lineno = lineno+1
                    join_line = continuation_parser.join_line(lines[lineno])
                line = "".join([str(line), str(join_line)])


            for c in self.ASSEMBLY_CHECKPOINTS:
                match = c.pattern_compiled.search(line)
                if match:
                    issues.append(RustInlineAsmIssue(filename,
                                            lineno=joined_lineno,
                                            checkpoint=c.pattern,
                                            description='' if not c.help else '\n' + c.help))
                    break

        #  intrinsics check
        for c in self.ARCH_INCOMPATIBLE_INTRINSICS:
            match = c.pattern_compiled.search(line)
            if match:
                issues.append(RustIntrinsicIssue(filename,
                                             lineno=joined_lineno,
                                             march=self.march,
                                             intrinsic=match.string.strip(),
                                             checkpoint=c.pattern,
                                             description='' if not c.help else '\n' + c.help))
                break

        return lineno

    def finalize_report(self, report):
        pass
