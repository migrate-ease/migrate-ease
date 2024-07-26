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

from advisor.html_report import HtmlReport
from advisor.report_factory import ReportOutputFormat

from advisor.arm64_config_guess_scanner import Arm64ConfigGuessScanner
from advisor.arm64_source_scanner import Arm64SourceScanner


class TestHtmlReport(unittest.TestCase):

    def test_item_icons(self):
        config_guess_scanner = Arm64ConfigGuessScanner()
        source_scanner = Arm64SourceScanner(ReportOutputFormat.HTML, arch='arm64')

        report = HtmlReport('/root', arch='arm64')

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

    def test_heading(self):
        report = HtmlReport('/home/user/source/application-1.0', arch='sw64')

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ofp:
            report.write(ofp)
            fname = ofp.name
            ofp.close()

            seenHeading = False

            with open(fname) as ifp:
                for line in ifp:
                    if 'Porting Readiness Report' in line and 'ApsaraStack' not in line:
                        self.assertIn('SW64', line)
                        seenHeading = True

            self.assertTrue(seenHeading)


if __name__ == '__main__':
    unittest.main()
