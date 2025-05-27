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

from common.localization import _

GOLANG_LINKLIBRARY = {'type': 'GolangLinkLibraryIssue', 'des': _("Use of libraries that are incompatible with the target platform")}
GOLANG_INLINE_ASM = {'type': 'GolangInlineAsmIssue',
                     'des': _("cgo: Use of inline assembly may lead to target platform compatibility issues")}
GOLANG_INTRINSIC = {'type': 'GolangIntrinsicIssue', 'des': _("cgo: Use of intrinsic functions that have compatibility issues with the target platform")}
GOLANG_CPP_STD_CODES = {'type': 'GolangCPPStdCodes', 'des': _("cgo: Compatibility issues or optimization opportunities related to Cpp source and memory order on the target platform")}
ASM = {'type': 'AsmIssue', 'des': _("Potentially architecture-specific assembly code in the source files that requires manual inspection")}

GOLANG_REPORT_TYPES = [
    GOLANG_LINKLIBRARY,
    GOLANG_INLINE_ASM,
    GOLANG_INTRINSIC,
    GOLANG_CPP_STD_CODES,
    ASM
]
