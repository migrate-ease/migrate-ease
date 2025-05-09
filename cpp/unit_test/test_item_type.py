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

import unittest

from common.error import Error
from common.issue import BaseReportItem

from advisor.arch_specific_library_issue import ArchSpecificLibraryIssue
from advisor.compiler_specific_issue import CompilerSpecificIssue
from advisor.intrinsic_issue import Avx256IntrinsicIssue, Avx512IntrinsicIssue, IntrinsicIssue
from advisor.no_equivalent_inline_asm_issue import NoEquivalentInlineAsmIssue
from advisor.no_equivalent_intrinsic_issue import NoEquivalentIntrinsicIssue
from advisor.ported_inline_asm_remark import PortedInlineAsmRemark
from advisor.report_item import ( COMPILER_SPECIFIC, ARCH_SPECIFIC_LIBRARY, INTRINSIC,
                                 AVX256_INTRINSIC, AVX512_INTRINSIC, NO_EQUIVALENT_INLINE_ASM,
                                 NO_EQUIVALENT_INTRINSIC, PORTED_INLINE_ASM_REMARK)


class TestItemType(unittest.TestCase):

    def test_compiler_specific_issue(self):
        issue = CompilerSpecificIssue('filename', 123, 'compiler', 'function')
        self.assertEqual(issue.issue_type, COMPILER_SPECIFIC)

    def test_arch_specific_library_issue(self):
        issue = ArchSpecificLibraryIssue('filename', 123, 'archSpecificLibrary', 'aarch64')
        self.assertEqual(issue.issue_type, ARCH_SPECIFIC_LIBRARY)

    def test_arch_specific_library_issue(self):
        issue = ArchSpecificLibraryIssue('filename', 123, 'archSpecificLibrary')
        self.assertEqual(issue.issue_type, ARCH_SPECIFIC_LIBRARY)

    def test_error(self):
        issue = Error('this is error', 'error', 123)
        self.assertEqual(issue.issue_type, BaseReportItem.ERROR)

    def test_intrinsic_issue(self):
        issue = IntrinsicIssue('filename', 123, 'aarch64', 'intrinsic')
        self.assertEqual(issue.issue_type, INTRINSIC)

    def test_avx256_intrinsic_issue(self):
        issue = Avx256IntrinsicIssue('filename', 123, 'aarch64', 'avx256intrinsic')
        self.assertEqual(issue.issue_type, AVX256_INTRINSIC)

    def test_avx512_intrinsic_issue(self):
        issue = Avx512IntrinsicIssue('filename', 123, 'aarch64', 'intrinsic')
        self.assertEqual(issue.issue_type, AVX512_INTRINSIC)

    def test_no_equivalent_inline_asm_issue(self):
        issue = NoEquivalentInlineAsmIssue('filename', 123, 'function')
        self.assertEqual(issue.issue_type, NO_EQUIVALENT_INLINE_ASM)

    def test_no_equivalent_intrinsic_issue(self):
        issue = NoEquivalentIntrinsicIssue('filename', 123, 'intrinsic', 'function')
        self.assertEqual(issue.issue_type, NO_EQUIVALENT_INTRINSIC)

    def test_ported_inline_asm_remark_issue(self):
        issue = PortedInlineAsmRemark(12)
        self.assertEqual(issue.issue_type, PORTED_INLINE_ASM_REMARK)


if __name__ == '__main__':
    unittest.main()
