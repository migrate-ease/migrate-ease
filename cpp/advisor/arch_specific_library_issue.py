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

from common.issue import Issue
from common.localization import _
from .report_item import ReportItem


class ArchSpecificLibraryIssue(Issue):

    def __init__(self, filename, lineno, lib_name, arch=None):

        if not arch:
            description = _("architecture-specific library is not available: lib%s") % lib_name
        else:
            description = _("architecture-specific library is not available on %s: lib%s") % (arch, lib_name)

        super().__init__(description=description,
                         filename=filename,
                         lineno=lineno,
                         issue_type=ReportItem.ARCH_SPECIFIC_LIBRARY)