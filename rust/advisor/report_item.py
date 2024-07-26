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
    RUST_LINKLIBRARY = {'type': 'RustLinkLibraryIssue', 'des': '检测到使用了和目标平台不兼容的库.'}
    RUST_INLINE_ASM = {'type': 'RustInlineAsmIssue', 'des': '检测到在目标平台中使用内联汇编, 可能存在平台兼容性问题.'}
    RUST_INTRINSIC = {'type': 'RustIntrinsicIssue', 'des': '检测到使用了和目标平台存在兼容性问题的 Intrinsic 函数.'}

    TYPES = BaseReportItem.TYPES + [
        RUST_LINKLIBRARY,
        RUST_INLINE_ASM,
        RUST_INTRINSIC]


Report.REPORT_ITEM = ReportItem
