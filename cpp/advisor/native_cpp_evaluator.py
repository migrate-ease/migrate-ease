import re
from enum import Enum


class State(Enum):
    SUPPORT = 1
    UNSUPPORT = 2
    UNKNOWN = 3
    INVALID = 4


class Token:
    def __init__(self, cal_priority, text):
        self.cal_priority = cal_priority
        self.text = text


class CommonConditionEvaluator:
    keywords = ['(', ')', '!', '&&', '||']
    DEFINED_RE = re.compile(r'(\s*)?defined\(\s*(\w+)\s*\)')
    END_COMMENT_RE = re.compile(r'//.*$')  # simple process of end comment in directive without consideration of ''

    def __init__(self, ARCH_SPECIFIC_MACRO_RE, NON_ARCH_SPECIFIC_MACRO_RE, SUPPORTED_COMPILER_MACROS_RE,
                 UNSUPPORTED_COMPILER_MACROS_RE):
        self.SUPPORTED_ARCH_MACROS_RE = ARCH_SPECIFIC_MACRO_RE
        self.UNSUPPORTED_ARCH_MACROS_RE = NON_ARCH_SPECIFIC_MACRO_RE
        self.SUPPORTED_COMPILER_MACROS_RE = SUPPORTED_COMPILER_MACROS_RE
        self.UNSUPPORTED_COMPILER_MACROS_RE = UNSUPPORTED_COMPILER_MACROS_RE
        self.compiler_error = False  # indicate the use of unsupported compiler without define()

    # calculate if the condition is not apparently supported
    def calculate(self, expression: str) -> State:
        match = self.__class__.END_COMMENT_RE.search(expression)
        if match is not None:
            expression = expression[:match.regs[0][0]].strip()
        tokens = self._lex(expression)
        return self._cal(tokens)

    def _lex(self, expression: str) -> list[Token]:
        expression = expression.lstrip().rstrip()
        tokens = []
        idx = 0

        while idx < len(expression):
            if expression[idx:].startswith('('):
                tokens.append(Token(4, '('))
                idx += 1
            elif expression[idx:].startswith(')'):
                tokens.append(Token(4, ')'))
                idx += 1
            elif expression[idx:].startswith('!'):
                tokens.append(Token(3, '!'))
                idx += 1
            elif expression[idx:].startswith('&&'):
                tokens.append(Token(2, '&&'))
                idx += 2
            elif expression[idx:].startswith('||'):
                tokens.append(Token(1, '||'))
                idx += 2
            while idx < len(expression) and expression[idx] == " ":
                idx += 1
            pre = idx
            while idx < len(expression) and (not self._is_keyword(expression[idx:])):
                idx += 1
            if pre != idx:
                tokens.append(Token(5, expression[pre:idx]))

        # ensure the token before ( and after ) is operator
        mapping = {}
        cnt = 1
        for i in range(len(tokens)):
            if tokens[i].text == '(':
                cnt += 1
                mapping[-cnt] = i
            elif tokens[i].text == ')':
                k = mapping[-cnt]
                mapping[k] = i
                cnt -= 1
        new_tokens = []
        idx = 0
        while idx < len(tokens):
            if tokens[idx].text == '(':
                pre = -1
                pos = -1
                if idx != 0 and tokens[idx - 1].cal_priority == 5:
                    new_tokens.pop(-1)
                    pre = idx - 1
                if mapping[idx] != len(tokens) - 1 and tokens[mapping[idx] + 1].cal_priority == 5:
                    pos = mapping[idx] + 1
                if pre != -1 or pos != -1:
                    if pre == -1:
                        pre = idx
                    if pos == -1:
                        pos = mapping[idx]
                    tmp = ""
                    for i in range(pre, pos + 1):
                        tmp += tokens[i].text
                    new_tokens.append(Token(5, tmp))
                    idx = pos + 1
                else:
                    new_tokens.append(tokens[idx])
                    idx += 1
            else:
                new_tokens.append(tokens[idx])
                idx += 1
        return new_tokens

    def _cal(self, tokens: list[Token]) -> State:
        define_list = []
        self.compiler_error = False
        stack_op = [Token(0, '$')]
        stack_val = []  # a stack value in enum(State)
        for token in tokens:
            if token.cal_priority == 5:
                match = self.__class__.DEFINED_RE.match(token.text)
                if match is not None:
                    text = match.group(2)
                    define_list.append(text)
                    if self.SUPPORTED_ARCH_MACROS_RE.match(text) is not None \
                            or self.SUPPORTED_COMPILER_MACROS_RE.match(text) is not None:
                        stack_val.append(State.SUPPORT)
                    else:
                        if self.UNSUPPORTED_ARCH_MACROS_RE.match(text) is not None \
                                or self.UNSUPPORTED_COMPILER_MACROS_RE.match(text) is not None:
                            stack_val.append(State.UNSUPPORT)
                        else:
                            stack_val.append(State.UNKNOWN)
                else:
                    stack_val.append(State.UNKNOWN)
                    unsupported_arch_macro = self.UNSUPPORTED_ARCH_MACROS_RE.match(token.text)
                    unsupported_compiler_macro = self.UNSUPPORTED_COMPILER_MACROS_RE.match(token.text)
                    if unsupported_arch_macro is not None or unsupported_compiler_macro is not None:
                        stack_val[-1] = State.UNSUPPORT
                    if unsupported_arch_macro is not None and unsupported_arch_macro.group(0) not in define_list:
                        self.compiler_error = True
            elif token.text == '(':
                stack_op.append(token)
            elif token.text == ')':
                while stack_op[-1].text != '(':
                    self._sub_cal(stack_op, stack_val)
                    if stack_val[-1] == State.INVALID:
                        return State.INVALID
                stack_op.pop(-1)
            elif stack_op[-1].cal_priority < token.cal_priority:
                stack_op.append(token)
            else:
                while stack_op[-1].cal_priority >= token.cal_priority and stack_op[-1].text != '(':
                    self._sub_cal(stack_op, stack_val)
                    if stack_val[-1] == State.INVALID:
                        return State.INVALID
                stack_op.append(token)
        while len(stack_op) > 1:
            self._sub_cal(stack_op, stack_val)
            if stack_val[-1] == State.INVALID:
                return State.INVALID
        if len(stack_val) != 1 or stack_val[-1] == State.INVALID:
            return State.INVALID
        return stack_val[0]

    def _sub_cal(self, stack_op, stack_val):
        op = stack_op.pop(-1)
        if op.text == '!':
            if len(stack_val) < 1:
                stack_val.append(State.INVALID)
            val = stack_val.pop(-1)
            if val == State.SUPPORT:
                stack_val.append(State.UNSUPPORT)
            elif val == State.UNSUPPORT:
                stack_val.append(State.SUPPORT)
            else:
                stack_val.append(State.UNKNOWN)
        elif op.text == '&&':
            if len(stack_val) < 2:
                stack_val.append(State.INVALID)
            val1 = stack_val.pop(-1)
            val2 = stack_val.pop(-1)
            if val1 == State.SUPPORT and val2 == State.SUPPORT:
                stack_val.append(State.SUPPORT)
            elif val1 == State.UNSUPPORT or val2 == State.UNSUPPORT:
                stack_val.append(State.UNSUPPORT)
            else:
                stack_val.append(State.UNKNOWN)
        else:
            if len(stack_val) < 2:
                stack_val.append(State.INVALID)
            val1 = stack_val.pop(-1)
            val2 = stack_val.pop(-1)
            if val1 == State.SUPPORT or val2 == State.SUPPORT:
                stack_val.append(State.SUPPORT)
            elif val1 == State.UNSUPPORT and val2 == State.UNSUPPORT:
                stack_val.append(State.UNSUPPORT)
            else:
                stack_val.append(State.UNKNOWN)
        return

    def _is_keyword(self, expr) -> bool:
        if expr.startswith('!='):
            return False
        for keyword in self.keywords:
            if expr.startswith(keyword):
                return True
        return False


class N2ConditionEvaluator:
    keywords = {'==': 3, '!=': 3, '>=': 3, '<=': 3, '>': 3, '<': 3, '&&': 2, '||': 1, '!': 4, '(': 5, ')': 5}
    DEFINED_RE = re.compile(r'defined\((\w+)\)')
    END_COMMENT_RE = re.compile(r'//.*$')  # simple process of end comment in directive without consideration of ''
    INT_RE = re.compile(r'^([0-9]+)L?')
    HEX_RE = re.compile(r'^0x([0-9a-fA-F]+)$')

    def __init__(self, defined_macros: dict, unsupported_macros_re):
        self.defined_macros = defined_macros
        self.unsupported_macros_re = unsupported_macros_re
        self.compiler_error = False

    def calculate(self, expression: str) -> State:
        match = self.__class__.END_COMMENT_RE.search(expression)
        if match is not None:
            expression = expression[:match.regs[0][0]].strip()
        tokens = self._lex(expression)
        return self._cal(tokens)

    def _lex(self, expression):
        idx = 0
        tokens = []
        while idx < len(expression):
            for keyword in self.__class__.keywords.keys():
                if expression[idx:].startswith(keyword):
                    tokens.append(Token(self.__class__.keywords[keyword], keyword))
                    idx += len(keyword)
            pre = idx
            while idx < len(expression) and (not self._is_keyword(expression[idx:])):
                idx += 1
            if pre != idx and expression[pre:idx].strip() != '':
                tokens.append(Token(6, expression[pre:idx].strip()))

        # merge function call, may be optimized since under real circumstance only deals with defined()
        mapping = {}
        cnt = 0
        for i in range(len(tokens)):
            if tokens[i].text == '(':
                cnt += 1
                mapping[-cnt] = i
            elif tokens[i].text == ')':
                k = mapping[-cnt]
                mapping[k] = i
                cnt -= 1
        new_tokens = []
        idx = 0
        while idx < len(tokens):
            if tokens[idx].text == '(':
                pre = -1
                pos = -1
                if idx != 0 and tokens[idx - 1].cal_priority == 6:
                    new_tokens.pop(-1)
                    pre = idx - 1
                if mapping[idx] != len(tokens) - 1 and tokens[mapping[idx] + 1].cal_priority == 6:
                    pos = mapping[idx] + 1
                if pre != -1 or pos != -1:
                    if pre == -1:
                        pre = idx
                    if pos == -1:
                        pos = mapping[idx]
                    tmp = ""
                    for i in range(pre, pos + 1):
                        tmp += tokens[i].text
                    new_tokens.append(Token(6, tmp))
                    idx = pos + 1
                else:
                    new_tokens.append(tokens[idx])
                    idx += 1
            else:
                new_tokens.append(tokens[idx])
                idx += 1
        return new_tokens

    def _cal(self, tokens) -> State:
        stack_op = [Token(0, '$')]
        stack_val = []    # a stack contains int, float, None and 'INVALID IN CALCULATION'
        for token in tokens:
            if token.cal_priority == 6:
                if self.__class__.INT_RE.match(token.text):
                    stack_val.append(int(self.__class__.INT_RE.match(token.text).group(1)))
                elif self.__class__.HEX_RE.match(token.text):
                    stack_val.append(int(self.__class__.HEX_RE.match(token.text).group(1),16))
                elif token.text in self.defined_macros.keys():
                    value = self.defined_macros[token.text]
                    if type(value) is int or type(value) is float:
                        stack_val.append(value)
                    else:
                        stack_val.append(None)
                else:
                    match = self.__class__.DEFINED_RE.match(token.text)
                    if match is not None:
                        if match.group(1) in self.defined_macros.keys():
                            stack_val.append(1)
                        elif self.unsupported_macros_re.match(match.group(1)):
                            stack_val.append(0)
                        else:
                            stack_val.append(None)
                    else:
                        stack_val.append(None)
            elif token.text == '(':
                stack_op.append(token)
            elif token.text == ')':
                while stack_op[-1].text != '(':
                    self._sub_cal(stack_op, stack_val)
                    if stack_val[-1] == 'INVALID IN CALCULATION！':
                        return State.INVALID
                stack_op.pop(-1)
            elif stack_op[-1].cal_priority < token.cal_priority:
                stack_op.append(token)
            else:
                while stack_op[-1].cal_priority >= token.cal_priority and stack_op[-1].text != '(':
                    self._sub_cal(stack_op, stack_val)
                    if stack_val[-1] == 'INVALID IN CALCULATION！':
                        return State.INVALID
                stack_op.append(token)
        while len(stack_op) > 1:
            self._sub_cal(stack_op, stack_val)
            if stack_val[-1] == 'INVALID IN CALCULATION！':
                return State.INVALID
        if len(stack_val) != 1 or stack_val[-1] == 'INVALID IN CALCULATION！':
            return State.INVALID
        if stack_val[0] is None:
            return State.UNKNOWN
        elif stack_val[0] == 0:
            return State.UNSUPPORT
        else:
            return State.SUPPORT

    def _sub_cal(self, stack_op, stack_val):
        op = stack_op.pop(-1)
        if op.text == '!':
            if len(stack_val) < 1:
                stack_val.append('INVALID IN CALCULATION！')
                return
            val = stack_val.pop(-1)
            if val is None:
                stack_val.append(None)
            elif val == 0:
                stack_val.append(1)
            else:
                stack_val.append(0)
        elif op.text == '&&':
            if len(stack_val) < 2:
                stack_val.append('INVALID IN CALCULATION！')
                return
            val1 = stack_val.pop(-1)
            val2 = stack_val.pop(-1)
            if val1 == 0 or val2 == 0:
                stack_val.append(0)
            elif val1 is None or val2 is None:
                stack_val.append(None)
            else:
                stack_val.append(1)
        elif op.text == '||':
            if len(stack_val) < 2:
                stack_val.append('INVALID IN CALCULATION！')
                return
            val1 = stack_val.pop(-1)
            val2 = stack_val.pop(-1)
            if (val1 != 0 and val1 is not None) or (val2 != 0 and val2 is not None):
                stack_val.append(1)
            elif val1 == 0 and val2 == 0:
                stack_val.append(0)
            else:
                stack_val.append(None)
        elif op.text == '>':
            if len(stack_val) < 2:
                stack_val.append('INVALID IN CALCULATION！')
                return
            val2 = stack_val.pop(-1)
            val1 = stack_val.pop(-1)
            if val1 is None or val2 is None:
                stack_val.append(None)
            elif val1 > val2:
                stack_val.append(1)
            else:
                stack_val.append(0)
        elif op.text == '<':
            if len(stack_val) < 2:
                stack_val.append('INVALID IN CALCULATION！')
                return
            val2 = stack_val.pop(-1)
            val1 = stack_val.pop(-1)
            if val1 is None or val2 is None:
                stack_val.append(None)
            elif val1 < val2:
                stack_val.append(1)
            else:
                stack_val.append(0)
        elif op.text == '>=':
            if len(stack_val) < 2:
                stack_val.append('INVALID IN CALCULATION！')
                return
            val2 = stack_val.pop(-1)
            val1 = stack_val.pop(-1)
            if val1 is None or val2 is None:
                stack_val.append(None)
            elif val1 >= val2:
                stack_val.append(1)
            else:
                stack_val.append(0)
        elif op.text == '<=':
            if len(stack_val) < 2:
                stack_val.append('INVALID IN CALCULATION！')
                return
            val2 = stack_val.pop(-1)
            val1 = stack_val.pop(-1)
            if val1 is None or val2 is None:
                stack_val.append(None)
            elif val1 <= val2:
                stack_val.append(1)
            else:
                stack_val.append(0)
        elif op.text == '==':
            if len(stack_val) < 2:
                stack_val.append('INVALID IN CALCULATION！')
                return
            val1 = stack_val.pop(-1)
            val2 = stack_val.pop(-1)
            if val1 is None or val2 is None:
                stack_val.append(None)
            elif val1 == val2:
                stack_val.append(1)
            else:
                stack_val.append(0)
        elif op.text == '!=':
            if len(stack_val) < 2:
                stack_val.append('INVALID IN CALCULATION！')
                return
            val1 = stack_val.pop(-1)
            val2 = stack_val.pop(-1)
            if val1 is None or val2 is None:
                stack_val.append(None)
            elif val1 != val2:
                stack_val.append(1)
            else:
                stack_val.append(0)
        else:
            stack_val.append('INVALID IN CALCULATION！')
        return

    def _is_keyword(self, expr) -> bool:
        if expr.startswith('!='):
            return False
        for keyword in self.keywords:
            if expr.startswith(keyword):
                return True
        return False
