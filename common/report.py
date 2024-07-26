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

import os
import typing

from .files_scanned_remark import FilesScannedRemark
from .issue import BaseReportItem
from .no_issues_found_remark import NoIssuesFoundRemark
from .scanner import BaseScanner


class Report:
    REPORT_ITEM: typing.Type[BaseReportItem] = None
    SCANNER: typing.Type[BaseScanner] = None
    # ISSUE_TYPES: typing.Type[BaseReportItem] = None

    def __init__(self,
                 root_directory,
                 arch=None,
                 march=None,
                 target_os=None,
                 output=None,
                 issue_type_config=None,
                 git_repo=None,
                 branch=None,
                 commit=None,
                 quiet=False,
                 progress=True):

        assert self.REPORT_ITEM is not None
        assert self.SCANNER is not None

        self.issues = []
        self.errors = []
        self.remarks = []
        self.root_directory = root_directory
        self.arch = arch
        self.march = march
        self.target_os = target_os
        self.output = output
        self.issue_type_config = issue_type_config
        self.git_repo = git_repo
        self.commit = commit
        self.branch = branch
        self.quiet = quiet
        self.progress = progress
        self.source_files = []
        self.source_dirs = set()

    def add_source_file(self, source_file):
        self.source_files.append(source_file)
        self.source_dirs.add(os.path.dirname(source_file))

    def add_issue(self, item):
        self.issues.append(item)

    def add_remark(self, item):
        self.remarks.append(item)

    def add_error(self, error):
        self.errors.append(error)

    def write(self, output_file, report_errors=False, report_remarks=False, include_summary=False):

        items = {}

        for issue_type in self.REPORT_ITEM.TYPES:
            items[issue_type.get('type')] = []

        all_items = []

        all_items += self.issues

        if report_remarks:
            all_items += self.remarks

        if report_errors:
            all_items += self.errors

        for item in all_items:
            items[item.issue_type.get('type')].append(item)

        if include_summary:
            items[self.REPORT_ITEM.SUMMARY.get('type')].append(
                FilesScannedRemark(len(self.source_files)))

            issue_type_except = [self.REPORT_ITEM.SUMMARY.get('type'),
                                 self.REPORT_ITEM.ERROR.get('type')]
            if not sum([len(items[type.get('type')]) for type in self.REPORT_ITEM.TYPES if
                        type.get('type') not in issue_type_except]) and report_remarks:
                items[self.REPORT_ITEM.NO_ISSUES_FOUND_REMARK.get('type')].append(NoIssuesFoundRemark())

        sorted_items = []

        for issue_type in self.REPORT_ITEM.TYPES:
            sorted_items += sorted(items[issue_type.get('type')], key=lambda item: (
                    (item.filename if item.filename else '') + ':' + item.description))

        self.write_items(output_file, sorted_items)

    def write_items(self, output_file, items):
        for item in items:
            print(item, file=output_file)
