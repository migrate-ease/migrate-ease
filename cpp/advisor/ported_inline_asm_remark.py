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
from .report_item import ReportItem


class PortedInlineAsmRemark(ReportItem):

    def __init__(self, ported_asm_source_files):

        description = _("%d inline assembly statements or intrinsics already have aarch64 equivalents") % ported_asm_source_files

        super().__init__(description=description,
                         issue_type=ReportItem.PORTED_INLINE_ASM_REMARK)
