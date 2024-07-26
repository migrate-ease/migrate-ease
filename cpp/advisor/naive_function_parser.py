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


class NaiveFunctionParser:

    """
    Naive function definition parser.
    """

    TYPE_RE = re.compile(r'[a-zA-Z_][a-zA-Z0-9_:]*$')

    #  Regular expression that matches function definitions.
    FUNCTION_RE = re.compile(r'(?:[a-zA-Z_][a-zA-Z0-9_:]*)\s+([a-zA-Z_][a-zA-Z0-9_:]*)\s*\(.*\)\s*{')

    #  White-listed C++ keywords that are definitely not function names.
    KEYWORDS = set(['catch',
                    'if',
                    'for',
                    'switch',
                    'while'])

    def __init__(self):

        #  Current function name, or None.
        self.current_function = None

        #  Previous line from a multi-line function declaration. e.g.:
        #  int
        #  myfunction
        #  (args)
        #  {
        #     ...
        #  }
        #
        self.previous_line = None

        #  Nesting depth of braces.
        self.nesting = 0

    def parse_line(self, line):
        """
        Parse function declarations in a source line.
        Multi-line declarations are supported so long as the follow the template:

        int
        myfunction
        (args)
        {

        Args:
            line (str): The line to parse.

        Returns:
            str: Current function name.
        """
        ret = None
        line = line.strip()

        if line.startswith('(') and self.previous_line:
            # function name is on previous line.
            function_line = self.previous_line + line

        elif line.startswith(')') and self.previous_line:
            # close of argument list
            function_line = self.previous_line + line

        elif line == '{' and self.previous_line:
            # opening brace is on its own line
            function_line = self.previous_line + line

        elif self.previous_line and (self.previous_line.endswith('(') or self.previous_line.endswith(',')):
            # multi line arguments
            function_line = self.previous_line + line

        elif self.previous_line and self.__class__.TYPE_RE.search(self.previous_line):
            # multi line return type
            function_line = self.previous_line + ' ' + line

        else:
            function_line = line

        if len(function_line) < 1000:  # length check to prevent running regexp on over-long lines
            match = self.__class__.FUNCTION_RE.search(function_line)
        else:
            match = None

        if match and not match.group(1) in self.__class__.KEYWORDS:
            ret = self.current_function = match.group(1)
            self.nesting = 1
            self.previous_line = None

        elif line.lstrip().startswith('{') or line.rstrip().endswith('{'):
            self.nesting += 1

        if line.lstrip().startswith('}') or line.rstrip().endswith('}'):
            self.nesting -= 1

        if self.nesting <= 0:
            self.nesting = 0
            self.current_function = None

        self.previous_line = function_line

        return ret
