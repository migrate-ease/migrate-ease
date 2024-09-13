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
import typing as t
from enum import Enum
from typing import Optional

from common.arch_strings import *
from common.arch_strings import N2_MARCH
from .native_cpp_evaluator import CommonConditionEvaluator, N2ConditionEvaluator, State


class CompilerCond(Enum):
    SUPPORTED_COMPILER = 'supported_compiler'
    UNSUPPORTED_COMPILER = 'unsupported_compiler'
    NOT_COMPILER = 'not_compiler'


class PreprocessorDirective(object):
    """
    Information about a preprocessor directive.

    The types of directives:
    ===
    TYPE_CONDITIONAL - a #if directive.
    TYPE_ERROR       - a #error directive.
    TYPE_PRAGMA      - a #pragma directive.
    TYPE_DEFINE      - a #define directive.
    TYPE_OTHER       - some other directive.
    TYPE_INVALID     - an invalid directive.
    """
    TYPE_CONDITIONAL = '#if'
    TYPE_ERROR = '#error'
    TYPE_PRAGMA = '#pragma'
    TYPE_DEFINE = '#define'
    TYPE_OTHER = 'other'
    TYPE_INVALID = 'invalid'

    parent: t.Optional['PreprocessorDirective']

    def __init__(self, directive_type: str,
                 if_line=None, is_compiler=CompilerCond.NOT_COMPILER, macro_name=None, body=None, is_start=True,
                 is_end=True, is_support=True, compiler_error=False):
        # self.incomplete = False
        self.is_support = is_support
        self.compiler_error = compiler_error

        self.is_start, self.is_end = is_start, is_end

        self.directive_type = directive_type

        #  The line that opened the current preprocessor block.
        self.if_line = if_line

        #  True if the current preprocessor block is compiler-specific, else
        #  False.
        #  self.is_compiler = is_compiler  # type: bool

        #  Macro name used in #ifdef, #define.
        self.macro_name = macro_name  # type: str

        #  define macro body.
        self.body = body  # type: str


class NaiveCpp(object):
    """
    Naive C preprocessor. This class is used by ClangSourceScanner to determine
    which source lines will/will not be compiled on target platforms.
    """

    #  Regular expression to tokenize C preprocessor directives.
    TOKENIZE_RE = re.compile(r'((?:!\s*)?defined\s*\(\s*\w+\s*\)|(?:!\s*)?\w+|\|\||\&\&|\(|\)|\s+)')

    #  Regular expression to match (possibly negated) defined(macro) expressions.
    DEFINED_RE = re.compile(r'(?:(!)\s*)?defined\s*\(\s*(\w+)\s*\)')

    #  Regular expression to match (possibly negated) macro expressions.
    MACRO_RE = re.compile(r'(?:(!)\s*)?(\w+)')

    #  Regular expression to match aarch64 predefined macros.
    AARCH64_MACROS_RE = re.compile(r'(?i)(?:\w*_|^)(%s)(?:_\w*|$)' % '|'.join(AARCH64_ARCHS))

    #  Regular expression to match non-aarch64 architecture predefined macros.
    NON_AARCH64_MACROS_RE = re.compile(r'(?i)(?:\w*_|^)(%s)(?:_\w*|$)' % '|'.join(NON_AARCH64_ARCHS))

    #  Regular expression to match compiler macros.
    SUPPORTED_COMPILER_MACROS_RE = re.compile(r'(?i)(?:\w*_?|^)(%s)(?:_?\w*|$)' % '|'.join(SUPPORTED_COMPILERS))
    ALL_COMPILER_MACROS_RE = re.compile(r'(?i)(?:\w*_?|^)(%s)(?:_?\w*|$)' % '|'.join(ALL_COMPILERS))
    UNSUPPORTED_COMPILER_MACROS_RE = re.compile(r'(?i)(?:\w*_?|^)(%s)(?:_?\w*|$)' % '|'.join(UNSUPPORTED_COMPILERS))

    #  Special-cased macros to ignore because they confuse the parser.
    IGNORE_MACROS = ['_M_HYBRID_X86_ARM64']

    N2_UNSUPPORTED_MACROS_RE = re.compile(r'(?i)(?:\w*_?|^)(%s)(?:_?\w*|$)'
                                              % str.join('|', YITAIN_UNSUPPORTED_COMPILERS + NON_AARCH64_ARCHS
                                                         + YITAIN_OTHER_UNSUPPORTED_MACROS))

    def __init__(self, arch: str, march: Optional[str], macros=None, warning_level=None):

        self.arch = arch
        self.march = march
        self.branches = [[State.SUPPORT]]
        self.macros = macros
        self.warning_level = warning_level
        self.level_state = [State.SUPPORT]

        if self.arch in AARCH64_ARCHS:

            self.ARCH_SPECIFIC_MACRO_RE = self.__class__.AARCH64_MACROS_RE
            self.NON_ARCH_SPECIFIC_MACRO_RE = self.__class__.NON_AARCH64_MACROS_RE

        else:
            raise RuntimeError('unknown arch: %s.' % self.arch)

        if self.arch == N2_MARCH:
            self.condition_evaluator = N2ConditionEvaluator(self.macros, self.N2_UNSUPPORTED_MACROS_RE)
        else:
            self.condition_evaluator = CommonConditionEvaluator(self.ARCH_SPECIFIC_MACRO_RE,
                                                                self.NON_ARCH_SPECIFIC_MACRO_RE,
                                                                self.SUPPORTED_COMPILER_MACROS_RE,
                                                                self.UNSUPPORTED_COMPILER_MACROS_RE)

        #  Stack of preprocessor block states. When a new preprocessor block is
        #  begun with #if or #ifdef a new state is pushed onto the stack. The
        #  state is True if the condition contains a macro defined on the self.arch,
        #  False if the condition contains the negation of a macro defined on
        #  self.arch, and None (undefined) otherwise. When the preprocessor block
        #  is finished with #endif the state is popped.
        self.in_arch: t.List[t.Optional[bool]] = []

        #  Stack of preprocessor block states. When a new preprocessor block is
        #  begun with #if or #ifdef a new state is pushed onto the stack. The
        #  state is True if the condition contains a macro defined on a
        #  non-self.arch architecture, False if the condition contains the
        #  negation of a macro defined on a non-self.arch architecture, and None
        #  (undefined) otherwise. When the preprocessor block is finished with
        #  #endif the state is popped.
        self.in_non_arch: t.List[t.Optional[bool]] = []

        #  Stack of preprocessor block states. When a new preprocessor block is
        #  begun with #if or #ifdef a new state is pushed onto the stack. The
        #  state is True if the condition contains a compiler-specific macro,
        #  else False.  When the preprocessor block is finished with #endif the
        #  state is popped.
        #  self.in_compiler = []  # type: List[Union[bool, None]]

        #  A stack of preprocessor block control statements. When a new
        #  preprocessor block is begun with #if or #ifdef the statement is
        #  pushed onto the stack. When the preprocessor block is finished with
        #  #endif the statement is popped.
        #  self.if_lines = []  # type: List[Union[bool, None]]

        #  Stack of preprocessor block states. Have we seen an self.arch-specific
        #  block at this level?
        #  self.seen_arch = []  # type: List[Union[bool, None]]

        #  Stack of preprocessor block states. Have we seen a
        #  non-self.arch-specific block at this level
        #  self.seen_non_arch = []  # type: List[Union[bool, None]]

        #  self.tree: t.List[PreprocessorDirective] = []

    def parse_line(self, line: str) -> t.Optional[PreprocessorDirective]:
        """
        Parse preprocessor directives in a source line.

        Args:
            line (str): The line to parse.

        Returns:
            PreprocessorDirective: Information about the parsed directive.
        """
        # if line.lstrip().startswith('#'):
        #     return self._parse_directive_line(line)
        # else:
        #     return None
        return self._parse_directive_line(line)

    def in_arch_specific_code(self):
        # type: () -> Union[bool, str]
        """
        Are we in arch specific code?

        Returns:
            bool: True if we are currently in an, e.g. #ifdef __aarch64__ or
            similar block, else False.
        """
        return self._in_x_code(self.in_arch)

    def in_other_arch_specific_code(self):
        # type: () -> Union[bool, str]
        """
        Are we in other architecture (non-aarch) specific code?

        Returns:
            bool: True if we are currently in an #ifdef OTHERARCH or similar
                  block, else False.
        """
        return self._in_x_code(self.in_non_arch)

    def in_other_arch_else_code(self):
        # type: () -> Union[bool, str]
        """
        Are we in the #else block of other architecture (e.g. non-aarch64)
        specific code?

        Returns:
            bool: True if we are currently in the #else block of an #ifdef
                  OTHERARCH or similar block, else False.
        """
        return self._in_x_else_code(self.in_non_arch)

    def in_compiler_specific_code(self):
        # type: () -> Union[bool, str]
        """
        Are we in compiler specific code?

        Returns:
            bool: True if we are currently in an #ifdef COMPILER or similar
                  block, else False.
        """
        return self._in_x_code(self.in_compiler)

    root: t.Optional[PreprocessorDirective] = None

    def _parse_directive_line(self, line: str) -> PreprocessorDirective:
        expression = line[1:].lstrip()
        parts = []
        if expression.startswith("if("):
            parts.append("if")
            parts.append(expression[2:])
        elif expression.startswith("elif("):
            parts.append("elif")
            parts.append(expression[4:])
        else:
            parts = expression.split(maxsplit=1)

        directive = parts[0]

        if directive == 'error':  # parts = ["#error", "erorr messages"]
            return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_ERROR)

        elif directive == 'pragma':  # parts = ["#pragma", "token string"]
            return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_PRAGMA)

        elif directive == 'define':  # parts = ["#define", "IDENTIFIER STATEMENT"]
            if len(parts) == 1:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_INVALID)

            rest = parts[1]
            if rest:
                define_parts = rest.lstrip().split(maxsplit=1)  # define_parts = ["IDENTIFIER", "STATEMENT"]

            macro_name = define_parts[0]
            body = define_parts[1] if len(define_parts) > 1 else None

            return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_DEFINE,
                                         macro_name=macro_name,
                                         body=body)

        elif directive == 'if':  # parts = ["#if", "EXPRESSION"]

            if len(parts) == 1:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_INVALID)

            expression = parts[1]

            state = self.condition_evaluator.calculate(expression)
            self.branches.append([state])
            self._update_level_state(True)

            if self.arch == N2_MARCH:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             is_start=True, is_end=False, if_line=line,
                                             is_support=self._get_support_state())

            if state == State.UNSUPPORT or self.level_state[-1] == State.UNSUPPORT:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL, is_support=False,
                                             is_start=True, is_end=False, if_line=line,
                                             compiler_error=self.condition_evaluator.compiler_error)
            else:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL, is_support=True,
                                             is_start=True, is_end=False, if_line=line,
                                             compiler_error=self.condition_evaluator.compiler_error)

        elif directive == 'elif':  # parts = ["#elif", "EXPRESSION"]

            if len(parts) == 1:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_INVALID)

            expression = parts[1]

            state = None
            for s in self.branches[-1]:
                if s == State.SUPPORT:
                    state = State.UNSUPPORT
            if state is None:
                state = self.condition_evaluator.calculate(expression)

            self.branches[-1].append(state)
            self._update_level_state(None)
            if self.arch == N2_MARCH:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             is_start=True, is_end=False, if_line=line,
                                             is_support=self._get_support_state())

            if state == State.UNSUPPORT or self.level_state[-1] == State.UNSUPPORT:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL, is_support=False,
                                             is_start=False, is_end=False, if_line=line,
                                             compiler_error=self.condition_evaluator.compiler_error)
            else:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL, is_support=True,
                                             is_start=False, is_end=False, if_line=line,
                                             compiler_error=self.condition_evaluator.compiler_error)

        elif directive == 'ifdef':  # parts = ["#ifdef", "IDENTIFIER"]

            if len(parts) == 1:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_INVALID)

            macro = parts[1]

            if self.arch == N2_MARCH:
                if macro in self.macros.keys():
                    self.branches.append([State.SUPPORT])
                elif self.N2_UNSUPPORTED_MACROS_RE.match(macro):
                    self.branches.append([State.UNSUPPORT])
                else:
                    self.branches.append([State.UNKNOWN])
                self._update_level_state(True)
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             if_line=line, is_support=self._get_support_state(),
                                             is_start=True, is_end=False)

            if self.NON_ARCH_SPECIFIC_MACRO_RE.match(macro) is not None \
                    or self.UNSUPPORTED_COMPILER_MACROS_RE.match(macro) is not None \
                    or self.level_state[-1] == State.UNSUPPORT:
                self.branches.append([State.UNSUPPORT])
                self._update_level_state(True)
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             if_line=line, is_support=False,
                                             is_start=True, is_end=False)
            else:
                if self.ARCH_SPECIFIC_MACRO_RE.match(macro) is not None \
                        or self.SUPPORTED_COMPILER_MACROS_RE.match(macro) is not None:
                    self.branches.append([State.SUPPORT])
                    self._update_level_state(True)
                else:
                    self.branches.append([State.UNKNOWN])
                    self._update_level_state(True)
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             if_line=line, is_support=True,
                                             is_start=True, is_end=False)

        elif directive == 'ifndef':  # parts = ["#ifndef", "IDENTIFIER"]

            if len(parts) == 1:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_INVALID)

            macro = parts[1]

            if self.arch == N2_MARCH:
                if macro in self.macros.keys():
                    self.branches.append([State.UNSUPPORT])
                elif self.N2_UNSUPPORTED_MACROS_RE.match(macro):
                    self.branches.append([State.SUPPORT])
                else:
                    self.branches.append([State.UNKNOWN])
                self._update_level_state(True)
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             if_line=line, is_support=self._get_support_state(),
                                             is_start=True, is_end=False)

            if self.ARCH_SPECIFIC_MACRO_RE.match(macro) is not None \
                    or self.SUPPORTED_COMPILER_MACROS_RE.match(macro) is not None \
                    or self.level_state[-1] == State.UNSUPPORT:
                self.branches.append([State.UNSUPPORT])
                self._update_level_state(True)
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             if_line=line, is_support=False,
                                             is_start=True, is_end=False)
            else:
                if self.NON_ARCH_SPECIFIC_MACRO_RE.match(macro) is not None \
                        or self.UNSUPPORTED_COMPILER_MACROS_RE.match(macro) is not None:
                    self.branches.append([State.SUPPORT])
                    self._update_level_state(True)
                else:
                    self.branches.append([State.UNKNOWN])
                    self._update_level_state(True)
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             if_line=line, is_support=True,
                                             is_start=True, is_end=False)

        elif directive == 'else':  # parts = ["#else"]
            s = State.SUPPORT
            for state in self.branches[-1]:
                if state == State.SUPPORT:
                    s = State.UNSUPPORT
                    break
                if state != State.UNSUPPORT:
                    s = State.UNKNOWN
            self.branches[-1].append(s)
            self._update_level_state(None)
            if self.arch == N2_MARCH:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             is_support=self._get_support_state(), is_start=False, is_end=True)

            if self.branches[-1][-1] == State.UNSUPPORT:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             is_support=False, is_start=False, is_end=True)
            else:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             is_support=True, is_start=False, is_end=True)

        elif directive == 'endif':
            self.branches.pop(-1)
            self._update_level_state(False)
            if self.arch == N2_MARCH:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             is_support=self._get_support_state(), is_start=False, is_end=True)

            if self.level_state[-1] == State.UNSUPPORT:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             is_start=False, is_end=True, is_support=False)
            else:
                return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CONDITIONAL,
                                             is_start=False, is_end=True, is_support=True)

        else:
            return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_OTHER)

    def _tri_negate(self, x):
        if x is None:
            return None
        else:
            return not x

    def _is_expression_x(self, expression, x):
        # type: (str, ...) -> Union[bool, None]

        # tokens = ["[!]defined(macro)", "||", "&&", "[!]macro", ...]
        tokens = self.__class__.TOKENIZE_RE.split(expression)

        for token in tokens:
            match = self.__class__.DEFINED_RE.match(token)

            if not match:
                match = self.__class__.MACRO_RE.match(token)

            if match:
                negated = match.group(1) == '!'
                macro = match.group(2)

                if macro in self.__class__.IGNORE_MACROS:
                    continue

                if x.match(macro) is not None:
                    return not negated
        return None

    def _is_expression_arch(self, expression):
        # type: (str) -> Union[bool, None]
        return self._is_expression_x(expression, self.ARCH_SPECIFIC_MACRO_RE)

    def _is_expression_non_arch(self, expression):
        # type: (str) -> Union[bool, None]
        return self._is_expression_x(expression, self.NON_ARCH_SPECIFIC_MACRO_RE)

    def _is_compiler(self, macro) -> CompilerCond:
        if self.__class__.SUPPORTED_COMPILER_MACROS_RE.match(macro):
            return CompilerCond.SUPPORTED_COMPILER
        elif self.__class__.ALL_COMPILER_MACROS_RE.match(macro):
            return CompilerCond.UNSUPPORTED_COMPILER
        else:
            return CompilerCond.NOT_COMPILER

    def _is_expression_compiler(self, expression) -> CompilerCond:
        if self._is_expression_x(expression, self.__class__.SUPPORTED_COMPILER_MACROS_RE):
            return CompilerCond.SUPPORTED_COMPILER
        elif self._is_expression_x(expression, self.__class__.ALL_COMPILER_MACROS_RE):
            return CompilerCond.UNSUPPORTED_COMPILER
        else:
            return CompilerCond.NOT_COMPILER

    def _in_x_code(self, x):
        return True in x

    def _in_x_else_code(self, x):
        return False in x

    def _get_support_state(self) -> bool:
        if self.warning_level == 'L1':
            if self.branches[-1][-1] == State.SUPPORT and self.level_state[-1] == State.SUPPORT:
                return True
            else:
                return False
        else:
            if self.branches[-1][-1] == State.UNSUPPORT or self.level_state[-1] == State.UNSUPPORT:
                return False
            else:
                return True

    def _update_level_state(self, in_stack):
        if in_stack is None:
            self.level_state.pop(-1)
            self._update_level_state(True)
        elif in_stack:
            if self.level_state[-1] == State.UNSUPPORT or self.branches[-1][-1] == State.UNSUPPORT:
                self.level_state.append(State.UNSUPPORT)
            elif self.level_state[-1] == State.SUPPORT and self.branches[-1][-1] == State.SUPPORT:
                self.level_state.append(State.SUPPORT)
            else:
                self.level_state.append(State.UNKNOWN)
        else:
            self.level_state.pop(-1)

