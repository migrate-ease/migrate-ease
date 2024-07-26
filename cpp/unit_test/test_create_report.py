import unittest

from advisor.report_factory import ReportFactory, ReportOutputFormat


class TestIssueTypeFilter(unittest.TestCase):
    def test_create_report(self):
        report_factory = ReportFactory()
        report = report_factory.createReport('./root', 'arm64')
        report = report_factory.createReport('./root', 'arm64', output_format=ReportOutputFormat.TEXT)
        report = report_factory.createReport('./root', 'arm64', False, True, False,
                                             output_format=ReportOutputFormat.HTML)
        report = report_factory.createReport('./root', 'arm64', output_format=ReportOutputFormat.CSV)
        report = report_factory.createReport('./root', 'arm64',
                                             output_format=ReportOutputFormat.CSV_ISSUE_TYPE_COUNT_BY_FILE)
        report = report_factory.createReport('./root', 'arm64', output_format=ReportOutputFormat.JSON)

    @unittest.expectedFailure
    def test_createfail_report(self):
        report_factory = ReportFactory()
        report = report_factory.createReport('./root', 'arm64', output_format='aaa')


if __name__ == '__main__':
    unittest.main()
