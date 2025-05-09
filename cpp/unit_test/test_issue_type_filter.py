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

from common.issue_type_config import IssueTypeConfig
from common.issue_type_filter import IssueTypeFilter
from common.report import Report
from common.issue import BaseReportItem

from advisor.report_item import CPP_REPORT_TYPES
from advisor.inline_asm_issue import InlineAsmIssue
from advisor.issue_types import ISSUE_TYPES
from advisor.cpp_scanner import CppScanner


class TestIssueTypeFilter(unittest.TestCase):
    def test_finalize(self):
        Report.REPORT_ITEM = BaseReportItem
        Report.REPORT_ITEM.TYPES += CPP_REPORT_TYPES
        Report.SCANNER = CppScanner
        report = Report('/root')

        issue_type_config = IssueTypeConfig(None)
        issue_type_filter = IssueTypeFilter(issue_type_config)
        issue_type_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test.c', 123))
        issue_type_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 1)

        report = Report('/root')
        issue_type_config = IssueTypeConfig('-InlineAsm', ISSUE_TYPES)
        issue_type_filter = IssueTypeFilter(issue_type_config)
        issue_type_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test.c', 123))
        issue_type_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

        report = Report('/root')
        issue_type_config = IssueTypeConfig('InlineAsm', ISSUE_TYPES)
        issue_type_filter = IssueTypeFilter(issue_type_config)
        issue_type_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test.c', 123))
        issue_type_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 1)

        report = Report('/root')
        issue_type_config = IssueTypeConfig('PreprocessorError', ISSUE_TYPES)
        issue_type_filter = IssueTypeFilter(issue_type_config)
        issue_type_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test.c', 123))
        issue_type_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

        report = Report('/root')
        issue_type_config = IssueTypeConfig('aaa', ISSUE_TYPES)
        issue_type_filter = IssueTypeFilter(issue_type_config)
        issue_type_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test.c', 123))
        issue_type_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

        report = Report('/root')
        issue_type_config = IssueTypeConfig(',PreprocessorError', ISSUE_TYPES)
        issue_type_filter = IssueTypeFilter(issue_type_config)
        issue_type_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test.c', 123))
        issue_type_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 0)


if __name__ == '__main__':
    unittest.main()
