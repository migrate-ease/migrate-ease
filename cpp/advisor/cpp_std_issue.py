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
from .report_item import CPP_STD_CODES


class CPPStdCodesIssue(Issue):

    def __init__(self, filename, lineno, arch=None, intrinsic=None, item_type=CPP_STD_CODES, checkpoint=None, description=None):

        if not description:
            description = _("cpp standard language check")

        super().__init__(description=description,
                         filename=filename,
                         lineno=lineno,
                         issue_type=CPP_STD_CODES,
                         checkpoint=checkpoint)
