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

from common.report import Report
from common.issue import BaseReportItem

from advisor.report_item import CPP_REPORT_TYPES
from advisor.config_guess_issue import ConfigGuessIssue
from advisor.inline_asm_issue import InlineAsmIssue
from advisor.old_crt_issue import OldCrtIssue
from advisor.target_os_filter import TargetOsFilter


class TestTargetOsFilter(unittest.TestCase):

    def test_finalize(self):
        Report.REPORT_ITEM = BaseReportItem
        Report.REPORT_ITEM.TYPES += CPP_REPORT_TYPES

        report = Report('/root', target_os='linux')
        target_os_filter = TargetOsFilter()
        target_os_filter.initialize_report(report)
        report.add_source_file('test.c')

        report.add_issue(ConfigGuessIssue('test.c', remark="autoconf config.guess needs updating to recognize aarch64 architecture"))
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test-aarch64.c', 123))
        target_os_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 2)

        report = Report('/root', target_os='linux')
        target_os_filter = TargetOsFilter()
        target_os_filter.initialize_report(report)
        report.add_source_file('test.c')
        report.add_issue(OldCrtIssue('test.c', 123, 'libcmt.lib'))
        report.add_source_file('test.c')
        report.add_issue(InlineAsmIssue('test-aarch64.c', 123))
        target_os_filter.finalize_report(report)
        self.assertEqual(len(report.issues), 1)


if __name__ == '__main__':
    unittest.main()
