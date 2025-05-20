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

from common.naive_comment_parser import NaiveCommentParser


class TestNaiveCommentParser(unittest.TestCase):

    def test_parse_line(self):
        comment_parser = NaiveCommentParser()
        self.assertFalse(comment_parser.parse_line('is not a comment'))
        self.assertTrue(comment_parser.parse_line('// single line comment'))
        self.assertFalse(comment_parser.parse_line('is not a comment'))
        self.assertTrue(comment_parser.parse_line('/* start of multi line comment'))
        self.assertTrue(comment_parser.parse_line(' middle of multi line comment'))
        self.assertTrue(comment_parser.parse_line('end of multi line comment */'))
        self.assertFalse(comment_parser.parse_line('is not a comment'))
        self.assertTrue(comment_parser.parse_line('/* single line comment */'))
        self.assertFalse(comment_parser.parse_line('is not a comment'))
        self.assertFalse(comment_parser.parse_line('comment in /* middle of */ line'))
        self.assertTrue(comment_parser.parse_line('/*'))
        self.assertTrue(comment_parser.parse_line('multi-line comments'))
        self.assertTrue(comment_parser.parse_line('*/'))


if __name__ == '__main__':
    unittest.main()
