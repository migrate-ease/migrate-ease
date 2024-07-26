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

from advisor.report import Report
from advisor.sw64_config_guess_scanner import Sw64ConfigGuessScanner

from advisor.arm64_config_guess_scanner import Arm64ConfigGuessScanner


class TestConfigGuessScanner(unittest.TestCase):

    def test_accepts_file_arm64(self):
        config_guess_scanner = Arm64ConfigGuessScanner()
        self.assertFalse(config_guess_scanner.accepts_file('test'))
        self.assertTrue(config_guess_scanner.accepts_file('config.guess'))

    def test_scan_file_object_arm64(self):
        config_guess_scanner = Arm64ConfigGuessScanner()
        report = Report('/root')
        io_object = io.StringIO('xxx')
        config_guess_scanner.scan_file_object('config.guess',
                                              io_object,
                                              report)
        self.assertEqual(len(report.issues), 1)

        report = Report('/root')
        io_object = io.StringIO('aarch64:Linux')
        config_guess_scanner.scan_file_object('config.guess',
                                              io_object,
                                              report)
        self.assertEqual(len(report.remarks), 0)

    def test_accepts_file_sw64(self):
        config_guess_scanner = Sw64ConfigGuessScanner()
        self.assertFalse(config_guess_scanner.accepts_file('test'))
        self.assertTrue(config_guess_scanner.accepts_file('config.guess'))

    def test_scan_file_object_sw64(self):
        config_guess_scanner = Sw64ConfigGuessScanner()
        report = Report('/root')
        io_object = io.StringIO('xxx')
        config_guess_scanner.scan_file_object('config.guess',
                                              io_object,
                                              report)
        self.assertEqual(len(report.issues), 1)
        report = Report('/root')
        io_object = io.StringIO('sw64:Linux')
        config_guess_scanner.scan_file_object('config.guess',
                                              io_object,
                                              report)
        self.assertEqual(len(report.remarks), 0)


if __name__ == '__main__':
    unittest.main()
