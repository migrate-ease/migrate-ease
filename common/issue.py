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

import re
import textwrap

from common.localization import _


class BaseReportItem:
    NON_EMPTY_LINE_RE = re.compile(r'\S')

    SUMMARY = {'type': 'summary', 'des': 'SUMMARY'}
    OTHER = {'type': 'OtherIssue',
            'des': _("Issues exceeding the limit will be categorized as OtherIssue. when the issue count limit option is enabled")}
    ERROR = {'type': 'Error',
            'des': _("Exception encountered by the code scanning tool during the scanning process, not an issue with the code logic itself. User can ignore it.")}
    NO_ISSUES_FOUND_REMARK = {'type': 'NoIssuesFoundRemark', 'des': 'NO_ISSUES_FOUND_REMARK'}

    TYPES = [
        SUMMARY,
        OTHER,
        ERROR,
        NO_ISSUES_FOUND_REMARK]

    def __init__(self, description, filename=None, lineno=None, issue_type=OTHER, checkpoint=None):

        self.filename = filename
        self.lineno = lineno  # start from 1!!
        self.filename = filename
        self.description = description
        self.issue_type = issue_type
        self.checkpoint = checkpoint
        self.snippet = None

    def set_code_snippet(self, snippet):
        self.snippet = snippet

    def get_code_snippets(self, lines=None, with_highlights=True):
        snippets_size_in_line = 8  # number of non-empty lines above or below the issue line
        snippets = ""

        if not lines:
            with open(self.filename, 'r') as fp:
                lines = fp.readlines()

        lineno_offset = 1
        nonempty_snippet_line_count = 0
        while (nonempty_snippet_line_count < snippets_size_in_line):

            if (self.lineno - lineno_offset) > 0:

                current_line = lines[self.lineno - lineno_offset]

                if with_highlights:
                    snippets = current_line.replace('<', '&lt;') + snippets
                else:
                    snippets = current_line + snippets

                if bool(self.NON_EMPTY_LINE_RE.search(current_line)):
                    nonempty_snippet_line_count += 1

                lineno_offset += 1
            else:  # no more lines
                break

        if with_highlights:
            dedented_line = textwrap.dedent(lines[self.lineno]).replace('\n', '')

            highlighted_line = lines[self.lineno].replace(dedented_line,
                                                          "<font style='color:red;'>" + dedented_line.replace('<',
                                                                                                              '&lt;') + "</font>")
            snippets += highlighted_line
        else:
            snippets += lines[self.lineno]

        lineno_offset = 1
        nonempty_snippet_line_count = 0
        while (nonempty_snippet_line_count < snippets_size_in_line):

            if (self.lineno + lineno_offset) < len(lines):

                current_line = lines[self.lineno + lineno_offset]

                if with_highlights:
                    snippets += current_line.replace('<', '&lt;')
                else:
                    snippets += current_line

                if bool(self.NON_EMPTY_LINE_RE.search(current_line)):
                    nonempty_snippet_line_count += 1

                lineno_offset += 1
            else:
                break

        return textwrap.dedent(snippets)

    def __str__(self):

        #  TODO: for the moment only sw64 support the presentation of codes
        if self.snippet:

            if self.description:
                return '%(file)s:%(lineno)s (%(checkpoint)s): \nCode:\n%(snippet)s\nDescription:\n%(description)s' % {
                    'file': self.filename,
                    'lineno': self.lineno,
                    'checkpoint': self.checkpoint,
                    'snippet': self.snippet,
                    'description': self.description
                }
            else:
                return '%(file)s:%(lineno)s (%(checkpoint)s): \nCode:\n%(snippet)s' % {
                    'file': self.filename,
                    'lineno': self.lineno,
                    'checkpoint': self.checkpoint,
                    'snippet': self.snippet
                }

        elif self.lineno:

            if self.checkpoint:
                return '%(file)s:%(lineno)s (%(checkpoint)s): %(description)s' % {
                    'file': self.filename,
                    'lineno': self.lineno,
                    'checkpoint': self.checkpoint,
                    'description': self.description
                }
            else:
                return '%(file)s:%(lineno)s: %(description)s' % {
                    'file': self.filename,
                    'lineno': self.lineno,
                    'description': self.description
                }

        elif self.filename:

            if self.checkpoint:
                return '%(file)s (%(checkpoint)s): %(description)s' % {
                    'file': self.filename,
                    'checkpoint': self.checkpoint,
                    'description': self.description
                }
            else:
                return '%(file)s: %(description)s' % {
                    'file': self.filename,
                    'description': self.description
                }

        else:

            if self.checkpoint:
                return '%(checkpoint)s: %(description)s' % {
                    'checkpoint': self.checkpoint,
                    'description': self.description
                }
            else:
                return '%(description)s' % {
                    'description': self.description
                }


class Issue(BaseReportItem):
    """
    Base class for issues.
    """

    def __init__(self, description, filename=None, lineno=None, issue_type=BaseReportItem.OTHER, checkpoint=None):
        super().__init__(description,
                         filename=filename,
                         lineno=lineno,
                         issue_type=issue_type,
                         checkpoint=checkpoint)

    @classmethod
    def display_name(cls):
        """
        Return the display name for the given issue class.
        """
        return re.sub('Issue$', '', cls.__name__)
