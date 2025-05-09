import unittest

from common.report_factory import ReportFactory, ReportOutputFormat
from common.report import Report
from common.issue import BaseReportItem
from advisor.report_item import CPP_REPORT_TYPES
from advisor.cpp_scanner import CppScanner


class TestIssueTypeFilter(unittest.TestCase):
    def test_create_report(self):
        report_factory = ReportFactory()
        Report.REPORT_ITEM = BaseReportItem
        Report.REPORT_ITEM.TYPES += CPP_REPORT_TYPES
        Report.SCANNER = CppScanner
        report = report_factory.createReport('./root', 'aarch64')
        report = report_factory.createReport('./root', 'aarch64', output_format=ReportOutputFormat.TEXT)
        report = report_factory.createReport('./root', 'aarch64', False, True, False,
                                             output_format=ReportOutputFormat.HTML)
        report = report_factory.createReport('./root', 'aarch64', output_format=ReportOutputFormat.CSV)
        report = report_factory.createReport('./root', 'aarch64',
                                             output_format=ReportOutputFormat.CSV_ISSUE_TYPE_COUNT_BY_FILE)
        report = report_factory.createReport('./root', 'aarch64', output_format=ReportOutputFormat.JSON)

    @unittest.expectedFailure
    def test_createfail_report(self):
        report_factory = ReportFactory()
        report = report_factory.createReport('./root', 'aarch64', output_format='aaa')


if __name__ == '__main__':
    unittest.main()
