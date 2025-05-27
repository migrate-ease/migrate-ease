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

import unittest

from common.continuation_parser import ContinuationParser


class TestOsFilter(unittest.TestCase):

    def test_parse_line(self):
        continuation_parser = ContinuationParser()
        line = continuation_parser.parse_line('just a line')
        self.assertEqual(line, 'just a line')
        line = continuation_parser.parse_line('')
        self.assertEqual(line, '')
        line = continuation_parser.parse_line('#define MACRO \\')
        self.assertIsNone(line)
        line = continuation_parser.parse_line('first line of macro \\')
        self.assertIsNone(line)
        line = continuation_parser.parse_line('second line of macro')
        self.assertEqual(line, '#define MACRO first line of macro second line of macro')

    def test_join_line(self):
        continuation_parser = ContinuationParser()
        line = continuation_parser.join_line('p_->Print(absl::Substitute(')
        self.assertIsNone(line, '')
        line = continuation_parser.join_line(' R"(')
        self.assertIsNone(line, '')
        line = continuation_parser.join_line('#endif  // $0')
        self.assertIsNone(line, '')
        line = continuation_parser.join_line(')",')
        self.assertIsNone(line, '')
        line = continuation_parser.join_line('ifdef_identifier_))')
        self.assertEqual(line, 'p_->Print(absl::Substitute(R"(#endif  // $0)",ifdef_identifier_))')

    def test_join_line_not_join(self):
        # The parentheses used as string assignments should not be treated as counting parentheses
        continuation_parser = ContinuationParser()
        line = continuation_parser.join_line('mini_descriptor = "$1,((jG"')
        line = continuation_parser.join_line('f_identifier_')
        self.assertEqual(line, 'f_identifier_')
        line = continuation_parser.join_line('a = "(ahgn)"    // ( is a flag.')
        line = continuation_parser.join_line('do not join')
        self.assertEqual(line, 'do not join')

if __name__ == '__main__':
    unittest.main()
