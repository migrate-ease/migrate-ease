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

import datetime
import json

from jinja2 import Environment, PackageLoader

from common.report import Report


class HtmlReport(Report):
    """
    Generates an HTML report from a template.
    """

    def write(self, output_file, report_errors=True, report_remarks=True, include_summary=False):
        """
        Override write to report all items.
        """
        super().write(output_file,
                      report_errors=report_errors,
                      report_remarks=report_remarks,
                      include_summary=include_summary)

    def write_items(self, output_file, items):

        env = Environment(
            loader=PackageLoader('common', 'templates'),
            autoescape=True
        )

        template = env.get_template('advice.html')

        issue_type_count = {}
        issue_count = 0
        for issue_type in self.REPORT_ITEM.TYPES:
            if issue_type != self.REPORT_ITEM.NO_ISSUES_FOUND_REMARK and issue_type != self.REPORT_ITEM.SUMMARY:
                issue_type_count[issue_type["type"]] = 0

        for item in items:
            if item.issue_type != self.REPORT_ITEM.SUMMARY and item.issue_type != self.REPORT_ITEM.NO_ISSUES_FOUND_REMARK:
                issue_type_count[item.issue_type["type"]] += 1
                issue_count += 1

        if issue_count == 0:
            print("No issue found.")

        count = 0
        for file_type in self.SCANNER.FILE_SUMMARY:
            count += self.SCANNER.FILE_SUMMARY[file_type]['count']

        rendered = template.render(
            root_directory=self.root_directory,
            issue_count=issue_count,
            file_summary=self.SCANNER.FILE_SUMMARY,
            file_sum_count=count,
            date=datetime.datetime.now().strftime("%Y-%m-%d at %H:%M:%S"),
            march=self.march,
            quiet=self.quiet,
            progress=self.progress,
            output=self.output,
            issue_type_config=self.issue_type_config,
            target_os=self.target_os,
            items=json.dumps([item.__dict__ for item in items]),
            git_repo=self.git_repo,
            commit=self.commit,
            issue_type_count=issue_type_count,
            branch=self.branch)

        output_file.write(rendered)
