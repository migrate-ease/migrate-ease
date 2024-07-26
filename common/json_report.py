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

import json

from common.report import Report


class JsonReport(Report):
    lang: str = ''

    """
    Generates a JSON report.
    """

    def write_items(self, output_file, items):
        assert self.lang != ''

        # munge 'self' fields so it can be serialized
        self.source_dirs = list(self.source_dirs)

        issue_type_counts = {}
        issue_count = 0
        no_show_type = ["NoIssuesFoundRemark", "summary", "NoEquivalentInlineAsmIssue", "NoEquivalentIntrinsicIssue",
                        "NoEquivalentIssue"]
        for issue_type in self.REPORT_ITEM.TYPES:
            if issue_type.get('type') not in no_show_type:
                issue_type_counts[issue_type.get('type')] = {}
                issue_type_counts[issue_type.get('type')]['count'] = 0
                issue_type_counts[issue_type.get('type')]['des'] = issue_type.get('des')

        for item in items:
            if item.issue_type.get('type') not in no_show_type:
                issue_type_counts[item.issue_type.get('type')]['count'] += 1
                issue_count += 1

        if issue_count == 0:
            print("No issue found.")

        self.total_issue_count = issue_count
        self.file_summary = self.SCANNER.FILE_SUMMARY
        # self.date = datetime.datetime.now().strftime("%Y-%m-%d at %H:%M:%S")
        self.issues = [item.__dict__ for item in items]
        self.issue_summary = issue_type_counts
        self.language_type = self.lang

        # self.issues = [i.__class__.__name__ + ': ' + str(i) for i in self.issues]
        self.errors = [i.__class__.__name__ + ': ' + str(i) for i in self.errors]
        self.remarks = [i.__class__.__name__ + ': ' + str(i) for i in self.remarks]
        print(json.dumps(self.__dict__, sort_keys=True, indent=4), file=output_file)
