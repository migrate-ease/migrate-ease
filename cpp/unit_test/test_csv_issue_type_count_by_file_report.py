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

from advisor.csv_issue_type_count_by_file_report import CsvIssueTypeCountByFileReport
from advisor.issue_type_config import IssueTypeConfig
from advisor.report_factory import ReportOutputFormat

from advisor.arm64_config_guess_scanner import Arm64ConfigGuessScanner
from advisor.arm64_source_scanner import Arm64SourceScanner


class TestCsvIssueTypeCountByFileReport(unittest.TestCase):

    def test_output(self):
        config_guess_scanner = Arm64ConfigGuessScanner()
        source_scanner = Arm64SourceScanner(ReportOutputFormat.CSV_ISSUE_TYPE_COUNT_BY_FILE, arch='arm64')

        issue_type_config = IssueTypeConfig()
        report = CsvIssueTypeCountByFileReport('/root', issue_type_config=issue_type_config)

        report.add_source_file('test_preprocessor.c')
        io_object = io.StringIO('#if !defined(_M_IX86) && !defined(_M_X64)\n#error This header is specific to X86 and X64 targets\n#endif')
        source_scanner.scan_file_object('test_preprocessor.c',
                                        io_object,
                                        report)

        report.add_source_file('test_pragma.c')
        io_object = io.StringIO('#pragma simd')
        source_scanner.scan_file_object('test_pragma.c',
                                        io_object,
                                        report)

        report.add_source_file('test_compiler_specific.c')
        io_object = io.StringIO('#ifdef __GNUC__')
        source_scanner.scan_file_object('test_compiler_specific.c',
                                        io_object,
                                        report)

        report.add_source_file('test_inline_asm.c')
        io_object = io.StringIO('__asm__ __volatile__( "pause" : : : "memory" );')
        source_scanner.scan_file_object('test_inline_asm.c',
                                        io_object,
                                        report)

        report.add_source_file('test_intrinsic.c')
        io_object = io.StringIO('const __m128i result = _mm_shuffle_epi8(data, vecmask[desc][0])')
        source_scanner.scan_file_object('test_intrinsic.c',
                                        io_object,
                                        report)

        self.assertEqual(len(report.issues), 5)

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ofp:
            report.write(ofp)
            fname = ofp.name
            ofp.close()

            with open(fname) as ifp:
                csv_reader = csv.DictReader(ifp)
                seen_preprocessor = False
                seen_pragma = False
                seen_compiler_specific = False
                seen_inline_asm = False
                seen_intrinsic = False

                for row in csv_reader:
                    if 'test_preprocessor.c' in row['filename']:
                        seen_preprocessor = True
                        for (field, actual) in row.items():
                            print(row.items())
                            if field == 'filename':
                                continue
                            expected = '1' if field == 'PreprocessorError' else '0'
                            self.assertEqual(expected, actual)
                    elif 'test_pragma.c' in row['filename']:
                        seen_pragma = True
                        for (field, actual) in row.items():
                            if field == 'filename':
                                continue
                            expected = '1' if field == 'Pragma' else '0'
                            self.assertEqual(expected, actual)
                    elif 'test_compiler_specific.c' in row['filename']:
                        seen_compiler_specific = True
                        for (field, actual) in row.items():
                            if field == 'filename':
                                continue
                            expected = '1' if field == 'CompilerSpecific' else '0'
                            self.assertEqual(expected, actual)
                    elif 'test_inline_asm.c' in row['filename']:
                        seen_inline_asm = True
                        for (field, actual) in row.items():
                            if field == 'filename':
                                continue
                            expected = '1' if field == 'InlineAsm' else '0'
                            self.assertEqual(expected, actual)
                    elif 'test_intrinsic.c' in row['filename']:
                        seen_intrinsic = True
                        for (field, actual) in row.items():
                            if field == 'filename':
                                continue
                            expected = '1' if field == 'Intrinsic' else '0'
                            self.assertEqual(expected, actual)
                    else:
                        print(row)
                        self.fail('Unexpected row in CSV output')

                self.assertTrue(seen_preprocessor)
                self.assertTrue(seen_pragma)
                self.assertTrue(seen_compiler_specific)
                self.assertTrue(seen_inline_asm)
                self.assertTrue(seen_intrinsic)


if __name__ == '__main__':
    unittest.main()
