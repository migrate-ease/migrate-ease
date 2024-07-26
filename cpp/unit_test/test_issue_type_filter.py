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
from advisor.issue_type_filter import IssueTypeFilter
from advisor.report import Report

from advisor.inline_asm_issue import InlineAsmIssue


class TestIssueTypeFilter(unittest.TestCase):
    def test_finalize(self):
        report = Report('/root')
        issue_type_config = IssueTypeConfig(None)
        issue_type_filter = IssueTypeFilter(issue_type_config)
        issue_type_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test.c', 123))
        issue_type_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 1)

        report = Report('/root')
        issue_type_config = IssueTypeConfig('-InlineAsm')
        issue_type_filter = IssueTypeFilter(issue_type_config)
        issue_type_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test.c', 123))
        issue_type_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

        report = Report('/root')
        issue_type_config = IssueTypeConfig('InlineAsm')
        issue_type_filter = IssueTypeFilter(issue_type_config)
        issue_type_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test.c', 123))
        issue_type_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 1)

        report = Report('/root')
        issue_type_config = IssueTypeConfig('PreprocessorError')
        issue_type_filter = IssueTypeFilter(issue_type_config)
        issue_type_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test.c', 123))
        issue_type_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

        report = Report('/root')
        issue_type_config = IssueTypeConfig('aaa')
        issue_type_filter = IssueTypeFilter(issue_type_config)
        issue_type_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test.c', 123))
        issue_type_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

        report = Report('/root')
        issue_type_config = IssueTypeConfig(',PreprocessorError')
        issue_type_filter = IssueTypeFilter(issue_type_config)
        issue_type_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test.c', 123))
        issue_type_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 0)


if __name__ == '__main__':
    unittest.main()
