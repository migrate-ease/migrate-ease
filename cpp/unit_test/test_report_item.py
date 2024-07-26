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


import tempfile
import unittest

from advisor.report_item import ReportItem


class TestReportItem(unittest.TestCase):

    def test_get_code_snippets(self):

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ofp:
            ofp.write("line0\nline1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10\n")
            fname = ofp.name
            ofp.close()

        report_item = ReportItem('description', fname, 5)
        self.assertIn('<font style=\'color:red;\'>line5</font>', report_item.get_code_snippets(''))

        report_item = ReportItem('', fname, 5)
        self.assertIn('<font style=\'color:red;\'>line5</font>', report_item.get_code_snippets(''))


if __name__ == '__main__':
    unittest.main()
