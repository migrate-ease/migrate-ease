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

    ARM_INCOMPATIBLE_INTRINSICS = []
    AARCH64_INLINE_ASSEMBLY_CHECKPOINTS = []
    AARCH64_GCC_INCOMPATIBLE_INTRINSICS = []
    AARCH64_CLANG_INCOMPATIBLE_INTRINSICS = []
    CPP_STD_CODES = []
    INCOMPATIBLE_HEADER_FILE = []
    N2_CLANG_INCOMPATIBLE_INTRINSICS = []
    N2_GCC_INCOMPATIBLE_INTRINSICS = []
    X86_PRAGMA = []

    def __init__(self, output_format, arch, march, compiler='gcc', warning_level='L1'):
        self.output_format = output_format
        self.arch = arch
        self.march = march
        self.compiler = compiler
        self.warning_level = warning_level
        self.check_state = True

        self.with_highlights = bool(
            output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)

        if self.arch == N2_MARCH or self.arch == AARCH64_ARCH:
            if self.arch == N2_MARCH:
                json_file = 'macros_n2.json'
            else:
                json_file= 'macros_aarch64.json'
            cur_dir = os.path.dirname(__file__)
            re_path = os.path.join('..', 'db', json_file)
            path = os.path.join(cur_dir, re_path)
            with open(path) as file:
                macros = json.load(file)
                self.macros = macros[self.compiler]

        self.load_checkpoints()

    def load_checkpoints(self):
        super().load_checkpoints()

        start_time = time.time()


        self.ARM_INCOMPATIBLE_INTRINSICS = init_checkpoints(
            self.checkpoints_content['X86_INTRINSICS'] +
            self.checkpoints_content['OTHER_ARCH_INTRINSICS'] +
            self.checkpoints_content['INCOMPATIBLE_UCRT_INTRINSICS'] +
            self.checkpoints_content['ARM_MSVC_INTRINSICS'] +
            self.checkpoints_content['AARCH64_GCC_INTRINSICS'] +
            self.checkpoints_content['AARCH64_NEON_INTRINSICS'] +
            self.checkpoints_content['AARCH64_MSVC_INTRINSICS'],
            self.checkpoints_content["COMMON_INTRINSICS"] + self.checkpoints_content["ARM_INTRINSICS"]
        )
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
        self.N2_GCC_INCOMPATIBLE_INTRINSICS = self.AARCH64_GCC_INCOMPATIBLE_INTRINSICS
        self.N2_CLANG_INCOMPATIBLE_INTRINSICS = self.AARCH64_CLANG_INCOMPATIBLE_INTRINSICS

        # please remember to remove lines for profiling after optimizing :)
        end_time = time.time()

        print('[C/C++] Initialization of checkpoints took %f seconds.' % (end_time - start_time))

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

        # migration to N2 need to pass the additional information
        if self.arch == N2_MARCH or self.arch == AARCH64_ARCH:
            naive_cpp = NaiveCpp(arch=self.arch, march=self.march, macros=self.macros,
                                 warning_level=self.warning_level)
        else:
            naive_cpp = NaiveCpp(arch=self.arch, march=self.march)

        PRAGMA_CHECKPOINTS: List[Checkpoint]

        if self.arch in AARCH64_ARCHS:
            if self.arch == N2_MARCH:
                if self.compiler == 'gcc':
                    ARCH_INCOMPATIBLE_INTRINSICS = self.N2_GCC_INCOMPATIBLE_INTRINSICS
                else:
                    ARCH_INCOMPATIBLE_INTRINSICS = self.N2_CLANG_INCOMPATIBLE_INTRINSICS
            elif self.arch == AARCH64_ARCH:
                if self.compiler == 'gcc':
                    ARCH_INCOMPATIBLE_INTRINSICS = self.AARCH64_GCC_INCOMPATIBLE_INTRINSICS
                else:
                    ARCH_INCOMPATIBLE_INTRINSICS = self.AARCH64_CLANG_INCOMPATIBLE_INTRINSICS
            else:
                ARCH_INCOMPATIBLE_INTRINSICS = self.ARM_INCOMPATIBLE_INTRINSICS
            ASSEMBLY_CHECKPOINTS = self.AARCH64_INLINE_ASSEMBLY_CHECKPOINTS
            PRAGMA_CHECKPOINTS = self.X86_PRAGMA

        else:

            ARCH_INCOMPATIBLE_INTRINSICS = None
            ASSEMBLY_CHECKPOINTS = None
            PRAGMA_CHECKPOINTS = None

        issues: List[Issue] = []
        lines = {lineno: line for lineno, line in enumerate(_lines, 1)}

        self.check_state = True

        # directive_stack: List[List[Issue]] = []

        for lineno in lines.keys():  # type: int, str

            line = lines[lineno]

            line = continuation_parser.parse_line(line)
            if not line or line.strip() == '' or line.strip() == '#':
                continue

            is_comment = comment_parser.parse_line(line)
            if is_comment:
                continue

            # result = naive_cpp.parse_line(line)  # type: PreprocessorDirective

            #  header file check
            if self.check_state:
                for c in self.INCOMPATIBLE_HEADER_FILE:
                    match = c.pattern_compiled.search(line)
                    if match:
                        issues.append(IncompatibleHeaderFileIssue(filename,
                                                                  lineno=find_matching_line_num(lines, lineno, c.pattern),
                                                                  checkpoint=c.pattern,
                                                                  description='' if not c.help else '\n' + c.help))
                        break

            # if the line is a PreprocessorDirective, process the possible '\' in the end
            # and combine to a complete macro for latter parsing.
            if line.lstrip().startswith('#'):
                result = naive_cpp.parse_line(line.strip())
                if result.directive_type == PreprocessorDirective.TYPE_DEFINE \
                        and result.body is not None and self.check_state:
                    self._check_clang(lines, lineno, line, naive_cpp, filename,
                                      ASSEMBLY_CHECKPOINTS, ARCH_INCOMPATIBLE_INTRINSICS, issues)
                self._check_directive(result, filename,
                                      lineno, line,
                                      function_parser, PRAGMA_CHECKPOINTS, issues)
            elif self.check_state:
                self._check_clang(lines, lineno, line, naive_cpp, filename,
                                  ASSEMBLY_CHECKPOINTS, ARCH_INCOMPATIBLE_INTRINSICS, issues)

            # if result:
            #     self._check_directive(result, filename, file_obj, report,
            #                           lineno, line,
            #                           function_parser, PRAGMA_CHECKPOINTS,
            #                           directive_stack, issues)
            # else:
            #     self._check_clang(lines, lineno, line, naive_cpp, filename,
            #                       ASSEMBLY_CHECKPOINTS, ARCH_INCOMPATIBLE_INTRINSICS, issues)

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

    def _check_clang(self,
                     # context
                     lines, lineno, line, naive_cpp, filename,
                     ASSEMBLY_CHECKPOINTS, ARCH_INCOMPATIBLE_INTRINSICS,
                     # results
                     issues: List[Issue]):
        # blank line
        if not lines[lineno].strip() or lines[lineno].strip() == '\n':
            return

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

            if match and not naive_cpp.in_other_arch_specific_code():
                issues.append(InlineAsmIssue(filename,
                                             lineno=lineno,
                                             checkpoint=c.pattern,
                                             description='' if not c.help else '\n' + c.help))
                break

        #  intrinsics check
        for c in ARCH_INCOMPATIBLE_INTRINSICS:
            match = c.pattern_compiled.search(line)
            if match and not naive_cpp.in_other_arch_specific_code():
                issues.append(IntrinsicIssue(filename,
                                             lineno=find_matching_line_num(lines, lineno, c.pattern),
                                             arch=self.arch,
                                             intrinsic=match.string.strip(),
                                             checkpoint=c.pattern,
                                             description='' if not c.help else '\n' + c.help))
                break

        #  cpp language check
        for c in self.CPP_STD_CODES:
            match = c.pattern_compiled.search(line)
            if match and not naive_cpp.in_other_arch_specific_code():
                # search for multiple lines
                if c.pattern_compiled.flags & re.MULTILINE:
                    multiple_lines = ''.join((lines.get(i, '') for i in range(lineno, lineno+3)))
                    match_multilines = c.pattern_compiled.search(multiple_lines)
                    if not match_multilines:
                        continue
                issues.append(CPPStdCodesIssue(filename,
                                               lineno=find_matching_line_num(lines, lineno, c.pattern),
                                               checkpoint=c.pattern,
                                               description='' if not c.help else '\n' + c.help))
                break
