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

from advisor.issue_type_config import IssueTypeConfig

from advisor.asm_source_issue import AsmSourceIssue
from advisor.compiler_specific_issue import CompilerSpecificIssue
from advisor.inline_asm_issue import InlineAsmIssue
from advisor.issue_types import ISSUE_TYPES
from advisor.no_equivalent_issue import NoEquivalentIssue
from advisor.pragma_issue import PragmaIssue
from advisor.preprocessor_error_issue import PreprocessorErrorIssue


class TestIssueTypeConfig(unittest.TestCase):
    def test_none(self):
        expected_issue_types = [issue_type for issue_type in ISSUE_TYPES.values()]
        issue_type_config = IssueTypeConfig(None)
        actual_issue_types = issue_type_config.filter_issue_types(ISSUE_TYPES)
        self.assertEqual(set(expected_issue_types), set(actual_issue_types))

        expected_included_issue = PreprocessorErrorIssue('foo', 'bar', 'wibble')
        self.assertTrue(issue_type_config.include_issue_p(expected_included_issue))

        expected_excluded_issue = CompilerSpecificIssue('foo', 'bar', 'wibble')
        self.assertTrue(issue_type_config.include_issue_p(expected_excluded_issue))

    def test_all(self):
        expected_issue_types = [issue_type for issue_type in ISSUE_TYPES.values()]
        issue_type_config = IssueTypeConfig('all')
        actual_issue_types = issue_type_config.filter_issue_types(ISSUE_TYPES)
        self.assertEqual(set(expected_issue_types), set(actual_issue_types))

        expected_included_issue = PreprocessorErrorIssue('foo', 'bar', 'wibble')
        self.assertTrue(issue_type_config.include_issue_p(expected_included_issue))

        expected_excluded_issue = CompilerSpecificIssue('foo', 'bar', 'wibble')
        self.assertTrue(issue_type_config.include_issue_p(expected_excluded_issue))

    def test_explicit_list(self):
        expected_issue_types = [PreprocessorErrorIssue, AsmSourceIssue, InlineAsmIssue]
        issue_type_config = IssueTypeConfig('PreprocessorError,AsmSource,InlineAsm')
        actual_issue_types = issue_type_config.filter_issue_types(ISSUE_TYPES)
        self.assertEqual(expected_issue_types, actual_issue_types)

        expected_included_issue = PreprocessorErrorIssue('foo', 'bar', 'wibble')
        self.assertTrue(issue_type_config.include_issue_p(expected_included_issue))

        expected_excluded_issue = CompilerSpecificIssue('foo', 'bar', 'wibble')
        self.assertFalse(issue_type_config.include_issue_p(expected_excluded_issue))

        expected_excluded_issue = PragmaIssue('foo', 'bar', 'wibble')  # not in explicit list
        self.assertFalse(issue_type_config.include_issue_p(expected_excluded_issue))

    def test_include(self):
        expected_issue_types = [issue_type for issue_type in ISSUE_TYPES.values()]
        issue_type_config = IssueTypeConfig('+CompilerSpecific')
        actual_issue_types = issue_type_config.filter_issue_types(ISSUE_TYPES)
        self.assertEqual(set(expected_issue_types), set(actual_issue_types))

        expected_included_issue = PreprocessorErrorIssue('foo', 'bar', 'wibble')
        self.assertTrue(issue_type_config.include_issue_p(expected_included_issue))

        expected_excluded_issue = NoEquivalentIssue('foo', 'bar', 'wibble')
        self.assertTrue(issue_type_config.include_issue_p(expected_excluded_issue))

    def test_exclude(self):
        def is_expected_filtered(issue_type):
            return issubclass(issue_type, PreprocessorErrorIssue)

        expected_issue_types = [issue_type for issue_type in ISSUE_TYPES.values() if not is_expected_filtered(issue_type)]
        issue_type_config = IssueTypeConfig('-PreprocessorError')
        actual_issue_types = issue_type_config.filter_issue_types(ISSUE_TYPES)
        self.assertEqual(set(expected_issue_types), set(actual_issue_types))

        expected_included_issue = PragmaIssue('foo', 'bar', 'wibble')
        self.assertTrue(issue_type_config.include_issue_p(expected_included_issue))

        expected_excluded_issue = PreprocessorErrorIssue('foo', 'bar', 'wibble')
        self.assertFalse(issue_type_config.include_issue_p(expected_excluded_issue))


if __name__ == '__main__':
    unittest.main()
