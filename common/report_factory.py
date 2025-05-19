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

from enum import Enum

from common.csv_issue_type_count_by_file_report import CsvIssueTypeCountByFileReport
from common.csv_report import CsvReport
from common.html_report import HtmlReport
from common.json_report import JsonReport
from common.text_report import TextReport


class ReportOutputFormat(Enum):
    AUTO = 'auto'
    CSV_ISSUE_TYPE_COUNT_BY_FILE = 'csv_issue_type_count_by_file'
    CSV = 'csv'
    JSON = 'json'
    HTML = 'html'
    TEXT = 'text'
    DEFAULT = AUTO


class ReportFactory:
    """
    Factory class for report output formats.
    """

    #  Dictionary mapping file extension to output format.  Used to decide the
    #  output format from the output file name when the report output format is
    #  'auto'.
    _OUTPUT_FORMAT_FOR_EXTENSION = {
        'json': ReportOutputFormat.JSON,
        'html': ReportOutputFormat.HTML,
        'htm': ReportOutputFormat.HTML,
        'txt': ReportOutputFormat.TEXT,
        'csv': ReportOutputFormat.CSV
    }

    def output_format_for_extension(self, extension):
        """
        Choose an output format based on the given file name extension.
        """
        return ReportFactory._OUTPUT_FORMAT_FOR_EXTENSION.get(extension.lower(), None)

    def createReport(self,
                     root_directory,
                     march=None,
                     target_os=None,
                     output=None,
                     output_format=ReportOutputFormat.JSON,
                     issue_type_config=None,
                     git_repo=None,
                     branch=None,
                     commit=None,
                     quiet=False,
                     progress=True):

        if output_format == ReportOutputFormat.TEXT:
            report = TextReport(root_directory)

        elif output_format == ReportOutputFormat.CSV:
            report = CsvReport(root_directory)

        elif output_format == ReportOutputFormat.CSV_ISSUE_TYPE_COUNT_BY_FILE:
            report = CsvIssueTypeCountByFileReport(root_directory,
                                                   issue_type_config=issue_type_config)

        elif output_format == ReportOutputFormat.HTML:
            report = HtmlReport(root_directory,
                                quiet=quiet,
                                progress=progress,
                                march=march,
                                output=output,
                                target_os=target_os,
                                issue_type_config=issue_type_config,
                                git_repo=git_repo,
                                commit=commit,
                                branch=branch)

        elif output_format == ReportOutputFormat.JSON:
            report = JsonReport(root_directory,
                                march=march,
                                target_os=target_os,
                                issue_type_config=issue_type_config,
                                git_repo=git_repo,
                                commit=commit,
                                branch=branch
                                )

        else:
            raise ValueError(output_format)

        return report
