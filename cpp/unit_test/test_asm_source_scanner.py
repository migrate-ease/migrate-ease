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
import unittest

from common.report_factory import ReportOutputFormat
from common.json_report import JsonReport
from common.report import Report
from common.issue import BaseReportItem

from advisor.arm64_asm_source_scanner import Arm64AsmSourceScanner
from advisor.report_item import CPP_REPORT_TYPES

class TestAsmSourceScanner(unittest.TestCase):

    def test_accepts_file_arm64(self):
        asm_source_scanner = Arm64AsmSourceScanner(ReportOutputFormat.JSON, march='armv8-a')
        self.assertFalse(asm_source_scanner.accepts_file('test.c'))
        self.assertFalse(asm_source_scanner.accepts_file('tests'))
        self.assertTrue(asm_source_scanner.accepts_file('test.s'))
        self.assertTrue(asm_source_scanner.accepts_file('test.S'))

    def test_scan_file_object_arm64(self):
        asm_source_scanner = Arm64AsmSourceScanner(ReportOutputFormat.JSON, march='armv8-a')

        Report.REPORT_ITEM = BaseReportItem
        Report.REPORT_ITEM.TYPES += CPP_REPORT_TYPES
        report = Report('/root')
        io_object = io.StringIO('__asm__("")')
        asm_source_scanner.scan_file_object('test.s', io_object, report)
        self.assertEqual(len(report.issues), 0)

        report = Report('/root')
        io_object = io.StringIO('__asm__("mov r0, r1")')
        asm_source_scanner.scan_file_object('test.s', io_object, report)
        self.assertEqual(len(report.issues), 1)

        report = Report('/root')
        io_object = io.StringIO('xxx\n/*__asm__("mov r0, r1")\nxxx')
        asm_source_scanner.scan_file_object('test.s', io_object, report)
        self.assertEqual(len(report.issues), 0)


if __name__ == '__main__':
    unittest.main()
