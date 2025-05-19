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
import json
import tempfile
import unittest

from common.issue_type_config import IssueTypeConfig
from common.json_report import JsonReport
from common.report_factory import ReportOutputFormat
from common.report import Report
from common.issue import BaseReportItem

from advisor.arm64_config_guess_scanner import Arm64ConfigGuessScanner
from advisor.arm64_source_scanner import Arm64SourceScanner
from advisor.report_item import CPP_REPORT_TYPES


class TestJsonReport(unittest.TestCase):

    def test_output(self):
        config_guess_scanner = Arm64ConfigGuessScanner(ReportOutputFormat.JSON, march='armv8-a')
        source_scanner = Arm64SourceScanner(ReportOutputFormat.JSON, march='armv8-a', compiler='gcc', warning_level='L1')

        issue_type_config = IssueTypeConfig()
        Report.REPORT_ITEM = BaseReportItem
        Report.REPORT_ITEM.TYPES += CPP_REPORT_TYPES
        report = JsonReport('/root', issue_type_config=issue_type_config)

        report.add_source_file('/root/src/test_inline_asm.c')
        io_object = io.StringIO('__asm__ __volatile__( "pause" : : : "memory" )')
        source_scanner.scan_file_object('test_inline_asm.c',
                                        io_object,
                                        report)

        report.add_source_file('/root/src/test_pragma_simd.c')
        io_object = io.StringIO('#pragma simd foo')
        source_scanner.scan_file_object('test_pragma_simd.c',
                                        io_object,
                                        report)

        report.add_source_file('/root/src/config.guess')
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
                json_top = json.load(ifp)

            self.assertIn('errors', json_top)
            self.assertEqual(len(json_top['errors']), 0)
            self.assertIn('issues', json_top)
            self.assertEqual(len(json_top['issues']), 3)
            self.assertIn('remarks', json_top)
            self.assertEqual(len(json_top['remarks']), 0)
            self.assertIn('issue_types', json_top)
            self.assertEqual(json_top['issue_types'], IssueTypeConfig.DEFAULT_FILTER)
            self.assertIn('target_os', json_top)
            self.assertIn(json_top['target_os'], ['linux', 'windows'])
            self.assertIn('root_directory', json_top)
            self.assertEqual(json_top['root_directory'], '/root')
            self.assertIn('source_dirs', json_top)
            self.assertEqual(len(json_top['source_dirs']), 1)
            self.assertEqual(json_top['source_dirs'][0], '/root/src')
            self.assertIn('source_files', json_top)
            self.assertEqual(len(json_top['source_files']), 3)
            seen_inline_asm = False
            seen_pragma = False
            seen_config_guess = False

            for fname in json_top['source_files']:

                if 'test_inline_asm.c' in fname:
                    seen_inline_asm = True
                elif 'test_pragma_simd.c' in fname:
                    seen_pragma = True
                elif 'config.guess' in fname:
                    seen_config_guess = True
                else:
                    self.fail('Unexpected source file name in JSON output')
            self.assertTrue(seen_inline_asm)
            self.assertTrue(seen_pragma)
            self.assertTrue(seen_config_guess)

    def test_issue_count_equals_zero(self):

        source_scanner = Arm64SourceScanner(ReportOutputFormat.JSON, march='armv8-a', compiler='gcc', warning_level='L1')

        issue_type_config = IssueTypeConfig()
        Report.REPORT_ITEM = BaseReportItem
        Report.REPORT_ITEM.TYPES += CPP_REPORT_TYPES
        JsonReport.lang = 'cpp'
        report = JsonReport('/root', issue_type_config=issue_type_config)

        report.add_source_file('/root/src/test.c')
        io_object = io.StringIO('xxx" )')
        source_scanner.scan_file_object('test.c',
                                        io_object,
                                        report)

        self.assertEqual(len(report.issues), 0)

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ofp:
            report.write(ofp)
            fname = ofp.name
            ofp.close()

        with open(fname) as ifp:
            json_top = json.load(ifp)

        self.assertEqual(json_top['issue_count'], 0)


if __name__ == '__main__':
    unittest.main()
