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

from common.issue import BaseReportItem
from common.report import Report


class ReportItem(BaseReportItem):
    PYTHON_LINKLIBRARY = {'type': 'PythonLinkLibraryIssue', 'des': '检测到使用了和目标平台不兼容的库.'}
    PYTHON_INLINE_ASM = {'type': 'PythonInlineAsmIssue',
                         'des': '检测到在目标平台中使用内联汇编, 可能存在平台兼容性问题.'}
    PYTHON_INTRINSIC = {'type': 'PythonIntrinsicIssue', 'des': '检测到使用了和目标平台存在兼容性问题的 Intrinsic 函数.'}
    PYTHON_PACKAGE = {'type': 'PythonPackageIssue', 'des': '检测到使用了和目标平台不兼容的 Package.'}

    TYPES = BaseReportItem.TYPES + [
        PYTHON_LINKLIBRARY,
        PYTHON_INLINE_ASM,
        PYTHON_INTRINSIC,
        PYTHON_PACKAGE]


Report.REPORT_ITEM = ReportItem
