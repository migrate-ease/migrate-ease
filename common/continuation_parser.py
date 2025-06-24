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


class ContinuationParser:

    """
    Continuation parser. Parses lines ending with \\ as continuations.
    """

    def __init__(self):
        self.continuation_line = None
        self.joined_line = None
        self.in_quotes = False
        self.open_parentheses_count = 0
        self.joined_lineno = -1

    def parse_line(self, line):
        """
        Parse continuations in a source line.

        Args:
            line (str): The line to parse.

        Returns:
            str: The concatenated line, or None if a continuation is in progress.
        """
        # Lines ending with \ are not processed immediately, but are
        # concatenated together until a line not ending in \ is encountered.
        # This means that issues reported against the line will have the line
        # number of the final continuation liner rather than the first.
        if line.endswith('\\') or line.endswith('\\\n'):
            if self.continuation_line:
                self.continuation_line += line.rstrip()[:-1]
            else:
                self.continuation_line = line.rstrip()[:-1]
            return None     # there will be more lines to come

        elif self.continuation_line:
            line = self.continuation_line + line
            self.continuation_line = None

        return line

    def join_line(self, line, lineno=None):
        """
        Parse continuations in a source line.

        Args:
            line (str): The line to parse.

        Returns:
            str: The concatenated line, or None if a continuation is in progress.
        """

        # Record the line number of the first line that is joined.
        # This is used to report the line number of the first line that is joined.
        if self.joined_lineno == -1 and lineno != None:
            self.joined_lineno = lineno

        # Traverse each line of the string, and use the parenthesis matching algorithm to
        # join multiple lines of code into a single string, increasing the accuracy of the match.
        for i, char in enumerate(line):
            # The parentheses used as string assignments should not be treated as counting parentheses.
            # e.g., a = "("
            if char == '"':
                if i > 0 and line[i-1] == '\\':
                    # If there is a '\' symbol before the double quote, then determine whether it is
                    # an escape character. If it is, it cannot be treated as a counted double quote.
                    # e.g., a = "ad\""
                    # Checks the number of backslashes before the double quote.
                    backslash_count = 0
                    index = i
                    while index > 0 and line[index-1] == '\\':
                        backslash_count += 1
                        index -= 1
                        # If there is an odd number of backslashes, the double quote is escaped.
                        if backslash_count % 2 == 1:
                            continue
                elif i > 0 and line[i-1] == "'" and i < len(line) -1:
                    # Characters enclosed in single quotes represent a character constant and cannot be treated
                    # as counted double quotes.
                    # e.g., a != '"'
                    if line[i+1] == "'":
                        continue
                self.in_quotes = not self.in_quotes
                continue

            if not self.in_quotes:
                if char == '/' and i < len(line)-1:
                    # Skip parsing comments to avoid issues with parentheses.
                    # e.g., a = (ahgn)    \\ ( is a flag.
                    if line[i+1] == '/':
                        break
                if char == '(':
                    self.open_parentheses_count += 1
                elif char == ')':
                    self.open_parentheses_count -= 1

        if self.open_parentheses_count != 0 or self.in_quotes:
            if self.joined_line:
                self.joined_line += line.strip()
            else:
                self.joined_line = line.strip()
            return None
        elif self.joined_line:
            line = self.joined_line + line
            self.joined_line = None
            self.in_quotes = False
            self.open_parentheses_count = 0
            try:
                # Script-generated strings can become excessively large after concatenation,
                # resulting in slow pattern matching (e.g., regex or search) due to increased computational complexity.
                if (len(line) > 2048):
                    raise ValueError("The concatenated result is too large to process!")
            except ValueError as e:
                print(e)
                return None
        return line
