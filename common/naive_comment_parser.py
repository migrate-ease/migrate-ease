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


class NaiveCommentParser:

    """
    Naive comment parser.
    """

    def __init__(self):
        #  Are we in a multi-line comment?
        self.in_comment = False

    def parse_line(self, line):
        """
        Parse comments in a source line.

        Args:
            line (str): The line to parse.

        Returns:
            bool: Is this line a comment?
        """
        if line.lstrip().startswith('//'):
            return True
        elif line.lstrip().startswith('/*'):
            if not line.lstrip().endswith('*/'):
                self.in_comment = True
            return True
        elif line.lstrip().endswith('*/'):
            if self.in_comment:
                self.in_comment = False
                return True

        if self.in_comment:
            return True

        return False
