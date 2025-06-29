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
import json
import os
import re
import time
from typing import List

from common.arch_strings import *
from common.checkpoint import Checkpoint, init_checkpoints
from common.continuation_parser import ContinuationParser
from common.find_port import find_matching_line_num
from common.issue import Issue
from common.report_factory import ReportOutputFormat

from .naive_comment_parser import NaiveCommentParser
from .cpp_scanner import CppScanner
from .cpp_std_issue import CPPStdCodesIssue
from .incompatible_header_file_issue import IncompatibleHeaderFileIssue
from .inline_asm_issue import InlineAsmIssue
from .intrinsic_issue import IntrinsicIssue
from .naive_cpp import NaiveCpp, PreprocessorDirective
from .naive_function_parser import NaiveFunctionParser
from .pragma_issue import PragmaIssue
from .preprocessor_error_issue import PreprocessorErrorIssue


class ClangSourceScanner(CppScanner):
    """
    Scanner that scans C, C++ and Fortran source files for potential porting
    issues.
    """

    # SOURCE_EXTENSIONS = ['.c', '.cc', '.cpp', '.cxx',
    #                      '.f', '.f77', '.f90', '.h',
    #                      '.hxx', '.hpp', '.i']

    C_SOURCE_EXTENSIONS = ['.c', '.h', '.i']
    CPP_SOURCE_EXTENSIONS = ['.cc', '.cpp', '.cxx', '.h', '.hxx', '.hpp', '.ii']

    AARCH64_INLINE_ASSEMBLY_CHECKPOINTS = []
    AARCH64_GCC_INCOMPATIBLE_INTRINSICS = []
    AARCH64_CLANG_INCOMPATIBLE_INTRINSICS = []
    CPP_STD_CODES = []
    INCOMPATIBLE_HEADER_FILE = []
    X86_PRAGMA = []

    INCOMPATIBLE_INTRINSICS = []
    ASSEMBLY_CHECKPOINTS = []
    PRAGMA_CHECKPOINTS = []

    inlineAsm_pattern = re.compile(r'\A(#define \S+)?\s*([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+[_]*inline[_]*)?(\s+[_]*goto[_]*)?')

    def __init__(self, output_format, march, compiler='gcc', warning_level='L1'):
        self.output_format = output_format
        self.march = march
        self.compiler = compiler
        self.warning_level = warning_level
        self.check_state = True

        self.with_highlights = bool(
            self.output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)

        if self.march in SUPPORTED_MARCH:
            if self.march == ARMV8_6_SVE2:
                json_file = 'macros_armv8.6-a+sve2.json'
            else:
                json_file= 'macros_armv8-a.json'
            cur_dir = os.path.dirname(__file__)
            re_path = os.path.join('..', 'db', json_file)
            path = os.path.join(cur_dir, re_path)
            with open(path) as file:
                macros = json.load(file)
                self.macros = macros[self.compiler]
        else:
            raise RuntimeError('unknown target processor architecuture: %s.' % self.march)

        self.load_checkpoints()
        self.set_checkpoints()

    def load_checkpoints(self):
        super().load_checkpoints()

        start_time = time.time()

        self.AARCH64_INLINE_ASSEMBLY_CHECKPOINTS = init_checkpoints(
            self.checkpoints_content["AARCH64_INLINE_ASSEMBLY_CHECKPOINTS"]
        )
        self.CPP_STD_CODES = init_checkpoints(
            self.checkpoints_content['CPP_STD_CODES']
        )
        self.INCOMPATIBLE_HEADER_FILE = init_checkpoints(
            self.checkpoints_content['INCOMPATIBLE_HEADER_FILE']
        )
        self.X86_PRAGMA = init_checkpoints(self.checkpoints_content['X86_PRAGMA'])
        self.AARCH64_GCC_INCOMPATIBLE_INTRINSICS = init_checkpoints(
            self.checkpoints_content['X86_INTRINSICS'] +
            self.checkpoints_content['OTHER_ARCH_INTRINSICS'] +
            self.checkpoints_content['INCOMPATIBLE_UCRT_INTRINSICS'] +
            self.checkpoints_content["ARM_INTRINSICS"] +
            self.checkpoints_content['ARM_MSVC_INTRINSICS'] +
            self.checkpoints_content['AARCH64_MSVC_INTRINSICS'],
            self.checkpoints_content["COMMON_INTRINSICS"] + self.checkpoints_content["AARCH64_GCC_INTRINSICS"]
        )
        self.AARCH64_CLANG_INCOMPATIBLE_INTRINSICS = init_checkpoints(
            self.checkpoints_content['X86_INTRINSICS'] +
            self.checkpoints_content['OTHER_ARCH_INTRINSICS'] +
            self.checkpoints_content['INCOMPATIBLE_UCRT_INTRINSICS'] +
            self.checkpoints_content["ARM_INTRINSICS"] +
            self.checkpoints_content['ARM_MSVC_INTRINSICS'] +
            self.checkpoints_content['AARCH64_MSVC_INTRINSICS'] +
            self.checkpoints_content['AARCH64_GCC_INTRINSICS'],
            self.checkpoints_content["COMMON_INTRINSICS"]
        )

        # please remember to remove lines for profiling after optimizing :)
        end_time = time.time()

        print('[C/C++] Initialization of checkpoints took %f seconds.' % (end_time - start_time))

    def set_checkpoints(self):
        if self.compiler == 'gcc':
            self.INCOMPATIBLE_INTRINSICS = self.AARCH64_GCC_INCOMPATIBLE_INTRINSICS
        else:
            self.INCOMPATIBLE_INTRINSICS = self.AARCH64_CLANG_INCOMPATIBLE_INTRINSICS
        self.ASSEMBLY_CHECKPOINTS = self.AARCH64_INLINE_ASSEMBLY_CHECKPOINTS
        self.PRAGMA_CHECKPOINTS = self.X86_PRAGMA

    def accepts_file(self, filename):

        _, ext = os.path.splitext(filename)
        return ext.lower() in self.__class__.C_SOURCE_EXTENSIONS or ext.lower() in self.__class__.CPP_SOURCE_EXTENSIONS

    # noinspection PyPep8Naming
    def scan_file_object(self, filename, file_obj, report):
        _lines = file_obj.readlines()
        _, ext = os.path.splitext(filename)

        if ext.lower() in self.__class__.C_SOURCE_EXTENSIONS:

            self.FILE_SUMMARY[self.C]['count'] += 1
            self.FILE_SUMMARY[self.C]['loc'] += len(_lines)

        elif ext.lower() in self.__class__.CPP_SOURCE_EXTENSIONS:

            self.FILE_SUMMARY[self.CPP]['count'] += 1
            self.FILE_SUMMARY[self.CPP]['loc'] += len(_lines)

        continuation_parser = ContinuationParser()
        comment_parser = NaiveCommentParser()
        function_parser = NaiveFunctionParser()

        naive_cpp = NaiveCpp(march=self.march, macros=self.macros,
                                 warning_level=self.warning_level)

        issues: List[Issue] = []
        lines = {lineno: line for lineno, line in enumerate(_lines, 1)}

        self.check_state = True
        # directive_stack: List[List[Issue]] = []
        lineno = 1
        while lineno <= len(lines.keys()):  # type: int, str
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

            #  header file check
            if self.check_state:
                for c in self.INCOMPATIBLE_HEADER_FILE:
                    match = c.pattern_compiled.search(line)
                    if match:
                        issues.append(IncompatibleHeaderFileIssue(filename,
                                                                  lineno=continuation_parser.joined_lineno,
                                                                  checkpoint=c.pattern,
                                                                  description='' if not c.help else '\n' + c.help))
                        break
            next_lineno=1
            # if the line is a PreprocessorDirective, process the possible '\' in the end
            # and combine to a complete macro for latter parsing.
            if line.lstrip().startswith('#'):
                result = naive_cpp.parse_line(line.strip())
                if result.directive_type == PreprocessorDirective.TYPE_DEFINE \
                        and result.body is not None and self.check_state:
                    next_lineno = self.check_clang(lines, line, lineno, continuation_parser.joined_lineno, filename,
                                                   InlineAsmIssue, IntrinsicIssue, CPPStdCodesIssue,
                                                   issues)
                self._check_directive(result, filename,
                                      lineno, line,
                                      function_parser, self.PRAGMA_CHECKPOINTS, issues)
            elif self.check_state:
                next_lineno = self.check_clang(lines, line, lineno, continuation_parser.joined_lineno, filename,
                                               InlineAsmIssue, IntrinsicIssue, CPPStdCodesIssue,
                                               issues)


            if next_lineno != 1:
                # check_clang already parses multiple lines of code, so there's no need to repeat the parsing logic here.
                lineno = next_lineno+1
            else:
                lineno += 1

            # reset the continuation parser's joined line number.
            continuation_parser.joined_lineno = -1

        # to extract code snippets
        for issue in issues:
            issue.set_code_snippet(issue.get_code_snippets(lines, with_highlights=self.with_highlights))
            report.add_issue(issue)

    def finalize_report(self, report):
        pass

    def _check_directive(self, result: PreprocessorDirective,
                         # context
                         filename, lineno, line, function_parser,
                         PRAGMA_CHECKPOINTS, issues: List[Issue]):
        # if result.incomplete:
        #     # parse incomplete
        #     pass
        if result.directive_type == PreprocessorDirective.TYPE_ERROR and self.check_state:
            issues.append(PreprocessorErrorIssue(filename,
                                                 lineno,
                                                 line.strip(),
                                                 checkpoint=function_parser.current_function))

        elif result.directive_type == PreprocessorDirective.TYPE_PRAGMA and self.check_state:
            for c in PRAGMA_CHECKPOINTS:
                match = c.pattern_compiled.search(line)
                if match:
                    issues.append(PragmaIssue(filename,
                                              lineno,
                                              line.strip(),
                                              checkpoint=function_parser.current_function))

        # #if/#elif/#ifdef/#ifndef/#else/#endif
        elif result.directive_type == PreprocessorDirective.TYPE_CONDITIONAL:
            # if result.compiler_error:
            #     issues.append(CompilerSpecificIssue(filename,
            #                                         lineno,
            #                                         result.if_line.strip(),
            #                                         checkpoint=function_parser.current_function))
            self.check_state = result.is_support

    def check_clang(self,
                     # context
                     lines, line, lineno, joined_lineno, filename,
                     InlineAsmIssue, IntrinsicIssue, CPPStdCodesIssue,
                     # results
                     issues: List[Issue]):
        continuation_parser = ContinuationParser()
        # inline assemly check.
        # Check for GCC/Clang inline asm (e.g., `asm volatile` or `__asm__`)
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
                    issues.append(InlineAsmIssue(filename,
                                            lineno=joined_lineno,
                                            checkpoint=c.pattern,
                                            description='' if not c.help else '\n' + c.help))
                    break

        #  intrinsics check
        for c in self.INCOMPATIBLE_INTRINSICS:
            match = c.pattern_compiled.search(line)
            if match:
                issues.append(IntrinsicIssue(filename,
                                             lineno=joined_lineno,
                                             march=self.march,
                                             intrinsic=match.string.strip(),
                                             checkpoint=c.pattern,
                                             description='' if not c.help else '\n' + c.help))
                break

        #  cpp language check
        for c in self.CPP_STD_CODES:
            match = c.pattern_compiled.search(line)
            if match:
                issues.append(CPPStdCodesIssue(filename,
                                               lineno=joined_lineno,
                                               checkpoint=c.pattern,
                                               description='' if not c.help else '\n' + c.help))
                break

        return lineno
