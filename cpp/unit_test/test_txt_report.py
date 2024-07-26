import tempfile
import unittest

from advisor.text_report import TextReport

from advisor.report_item import ReportItem


class TestTxtReport(unittest.TestCase):

    def test_write_report(self):
        report = TextReport('./root')
        item1 = ReportItem('description')
        report.add_issue(item1)
        item2 = ReportItem('description', function='function')
        report.add_issue(item2)
        item3 = ReportItem('description', filename='filename')
        report.add_issue(item3)
        item4 = ReportItem('description', function='function', filename='filename')
        report.add_issue(item4)
        item5 = ReportItem('description', function='function', filename='filename', lineno='12')
        report.add_issue(item5)
        item6 = ReportItem('description', lineno='12', filename='filename')
        report.add_issue(item6)
        item7 = ReportItem('description', function='function', filename='filename', lineno='12')
        item7.set_code_snippet("code")
        report.add_issue(item7)

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ofp:
            report.write(ofp)
            ofp.close()


if __name__ == '__main__':
    unittest.main()
