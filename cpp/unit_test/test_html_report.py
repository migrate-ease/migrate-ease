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

import io
import tempfile
import unittest

from common.html_report import HtmlReport
from common.report_factory import ReportOutputFormat
from common.report import Report
from common.issue import BaseReportItem
from advisor.report_item import CPP_REPORT_TYPES

from advisor.arm64_config_guess_scanner import Arm64ConfigGuessScanner
from advisor.arm64_source_scanner import Arm64SourceScanner


class TestHtmlReport(unittest.TestCase):

    def test_item_icons(self):
        config_guess_scanner = Arm64ConfigGuessScanner(ReportOutputFormat.HTML, march='armv8-a')
        source_scanner = Arm64SourceScanner(ReportOutputFormat.HTML, march='armv8-a', compiler='gcc', warning_level='L1')

        Report.REPORT_ITEM = BaseReportItem
        Report.REPORT_ITEM.TYPES += CPP_REPORT_TYPES
        report = HtmlReport('/root', march='armv8-a')

        io_object = io.StringIO(' __asm__ __volatile__( "pause" : : : "memory" )')
        source_scanner.scan_file_object('test_inline_asm.c',
                                        io_object,
                                        report)

        io_object = io.StringIO('#pragma simd foo')
        source_scanner.scan_file_object('test_pragma_simd.c',
                                        io_object,
                                        report)

        io_object = io.StringIO('xxx')
        config_guess_scanner.scan_file_object('config.guess',
                                              io_object,
                                              report)

        self.assertEqual(len(report.issues), 3)

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ofp:
            report.write(ofp)
            fname = ofp.name
            ofp.close()

            with open(fname) as ifp:
                seen_inline_asm_issue = False
                seen_pragma_issue = False
                seen_config_guess_issue = False

                for line in ifp:
                    if 'InlineAsmIssue' in line:
                        seen_inline_asm_issue = True
                    elif 'PragmaIssue' in line:
                        seen_pragma_issue = True
                    elif 'ConfigGuessIssue' in line:
                        seen_config_guess_issue = True

                self.assertTrue(seen_inline_asm_issue)
                self.assertTrue(seen_pragma_issue)
                self.assertTrue(seen_config_guess_issue)


if __name__ == '__main__':
    unittest.main()
