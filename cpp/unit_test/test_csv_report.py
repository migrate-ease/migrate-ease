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

import csv
import io
import tempfile
import unittest

from common.csv_report import CsvReport
from common.report_factory import ReportOutputFormat
from common.report import Report
from common.issue import BaseReportItem

from advisor.arm64_config_guess_scanner import Arm64ConfigGuessScanner
from advisor.arm64_source_scanner import Arm64SourceScanner
from advisor.report_item import CPP_REPORT_TYPES


class TestCsvReport(unittest.TestCase):

    def test_output(self):
        config_guess_scanner = Arm64ConfigGuessScanner(ReportOutputFormat.CSV, arch='aarch64', march='')
        source_scanner = Arm64SourceScanner(ReportOutputFormat.CSV, arch='aarch64', march='', compiler='gcc', warning_level='L1')

        Report.REPORT_ITEM = BaseReportItem
        Report.REPORT_ITEM.TYPES += CPP_REPORT_TYPES
        report = CsvReport('/root')

        report.add_source_file('test_inline_asm.c')
        io_object = io.StringIO('__asm__ __volatile__( "pause" : : : "memory" )')
        source_scanner.scan_file_object('test_inline_asm.c',
                                        io_object,
                                        report)

        report.add_source_file('test_pragma_simd.c')
        io_object = io.StringIO('#pragma simd')
        source_scanner.scan_file_object('test_pragma_simd.c',
                                        io_object,
                                        report)

        report.add_source_file('config.guess')
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
                csv_reader = csv.DictReader(ifp)
                seen_issue1 = False
                seen_issue2 = False
                seen_issue3 = False

                for row in csv_reader:
                    if 'test_inline_asm.c' in row['filename']:
                        self.assertIn('InlineAsm', row['issue_type'])
                        seen_issue1 = True
                    elif 'test_pragma_simd.c' in row['filename']:
                        self.assertIn('Pragma', row['issue_type'])
                        seen_issue2 = True
                    elif 'config.guess' in row['filename']:
                        self.assertIn('ConfigGuess', row['issue_type'])
                        seen_issue3 = True
                    else:
                        self.fail('Unexpected row in CSV output')

                self.assertTrue(seen_issue1)
                self.assertTrue(seen_issue2)
                self.assertTrue(seen_issue3)


if __name__ == '__main__':
    unittest.main()
