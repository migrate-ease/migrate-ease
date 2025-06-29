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

#class ReportItem(BaseReportItem):
PYTHON_LINKLIBRARY = {'type': 'PythonLinkLibraryIssue', 'des': _('Use of libraries that are incompatible with the target platform')}
PYTHON_INLINE_ASM = {'type': 'PythonInlineAsmIssue',
                     'des': _("cffi: Use of inline assembly in the target platform may lead to compatibility issues")}
PYTHON_INTRINSIC = {'type': 'PythonIntrinsicIssue', 'des': _("cffi: Use of intrinsic functions that have compatibility issues with the target platform")}
PYTHON_CPP_STD_CODES = {'type': 'PythonCPPStdCodes', 'des': _("cffi: Compatibility issues or optimization opportunities related to Cpp source and memory order on the target platform")}
PYTHON_PACKAGE = {'type': 'PythonPackageIssue', 'des': _("Use of packages that are incompatible with the target platform")}

PYTHON_REPORT_TYPES = [
    PYTHON_LINKLIBRARY,
    PYTHON_INLINE_ASM,
    PYTHON_INTRINSIC,
    PYTHON_CPP_STD_CODES,
    PYTHON_PACKAGE
]
