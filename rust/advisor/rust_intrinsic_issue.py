"""
Copyright 2020-2023 Alibaba Inc.

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
from .report_item import RUST_INTRINSIC


class RustIntrinsicIssue(Issue):

    def __init__(self, filename, lineno, march=None, intrinsic=None, issue_type=RUST_INTRINSIC, checkpoint=None, description=None):

        if not description:
            description = _("Intrinsic not supported on %s: %s") % (march, intrinsic)

        super().__init__(description=description,
                         filename=filename,
                         lineno=lineno,
                         issue_type=issue_type,
                         checkpoint=checkpoint)
