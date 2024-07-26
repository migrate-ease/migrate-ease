"""
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
from .cross_compile_issue import CrossCompileIssue
from .report_item import ReportItem


class SignedCharIssue(CrossCompileIssue):

    def __init__(self, filename, lineno, description=None):

        if not description:
            description = _("It's recommended that you use the compiler command option \'-fsigned-char\' changes the default behaviour of plain char to be a signed char.")

        super().__init__(description=description,
                         filename=filename,
                         lineno=lineno,
                         issue_type=ReportItem.SIGNED_CHAR)
