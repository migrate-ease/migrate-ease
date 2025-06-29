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
from .report_item import IMAGE


class ImageIssue(Issue):

    def __init__(self, filename, lineno, march=None, image=None, issue_type=IMAGE, checkpoint=None, description=None):

        if not description:
            description = _("The dockerfile is build based on the Base Image:%s, \
please confirm whether the Base Image supports the architecture: %s by scanning the dockerfile of the Base Image \
or by yourself.") % (image, march)

        super().__init__(description=description,
                         filename=filename,
                         lineno=lineno,
                         issue_type=issue_type,
                         checkpoint=checkpoint)