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

from .cpp_scanner import CppScanner
from .old_crt_issue import OldCrtIssue


class TargetOsFilter(CppScanner):

    """
    Filters out issues that are only applicable to other operating
    systems.
    """

    def finalize_report(self, report):
        def target_os_matches(issue, target_os):
            if target_os == 'all':
                return True
            if isinstance(issue, OldCrtIssue) and \
                    target_os != 'windows':
                return False

            return True

        report.issues = [issue for issue in report.issues
                         if target_os_matches(issue, report.target_os)]
