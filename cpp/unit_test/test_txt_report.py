import tempfile
import unittest

from common.text_report import TextReport
from common.issue import Issue
from common.report import Report
from common.issue import BaseReportItem

from advisor.report_item import CPP_REPORT_TYPES
from advisor.cpp_scanner import CppScanner


class TestTxtReport(unittest.TestCase):

    def test_write_report(self):
        Report.REPORT_ITEM = BaseReportItem
        Report.REPORT_ITEM.TYPES += CPP_REPORT_TYPES
        Report.SCANNER = CppScanner
        report = TextReport('./root')
        item1 = Issue('description')
        report.add_issue(item1)
        item2 = Issue('description', filename='filename')
        report.add_issue(item2)
        item3 = Issue('description', filename='filename', lineno='12')
        item3.set_code_snippet("code")
        report.add_issue(item3)

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ofp:
            report.write(ofp)
            ofp.close()


if __name__ == '__main__':
    unittest.main()
