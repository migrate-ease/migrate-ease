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

from common.localization import _
from common.issue import BaseReportItem


class OtherIssues(BaseReportItem):

    def __init__(self, filename, count):

        description = _("%d other issues") % count

        super().__init__(description=description,
                         filename=filename,
                         issue_type=BaseReportItem.OTHER)
