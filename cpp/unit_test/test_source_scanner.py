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

import io
import tempfile
import unittest

from advisor.report import Report
from advisor.report_factory import ReportOutputFormat
from advisor.scanner import Scanner
from advisor.sw64_source_scanner import Sw64SourceScanner

from advisor.arm64_source_scanner import Arm64SourceScanner
from advisor.report_item import ReportItem


class TestSourceScanner(unittest.TestCase):
    def setUp(self):
        self.source_scanner = Arm64SourceScanner(output_format=ReportOutputFormat.HTML, arch='arm64')

    def tearDown(self):
        pass

    def test_scan_file_error(self):

        def raise_base_exception():
            raise BaseException

        def raise_keyboard_interrupt():
            raise KeyboardInterrupt

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ofp:
            ofp.write("test")
            fname = ofp.name

            report = Report('/root')
            self.source_scanner.scan_file_object = raise_base_exception
            self.source_scanner.scan_file(fname,
                                          report)
            self.assertEqual(len(report.errors), 1)

            report = Report('/root')
            self.source_scanner.scan_file_object = raise_keyboard_interrupt
            self.source_scanner.scan_file(fname,
                                          report)
            self.assertEqual(len(report.errors), 1)

    def test_accepts_file_arm64(self):
        self.assertFalse(self.source_scanner.accepts_file('test'))
        self.assertTrue(self.source_scanner.accepts_file('test.c'))
        self.assertTrue(self.source_scanner.accepts_file('test.cc'))
        self.assertTrue(self.source_scanner.accepts_file('test.CC'))
        self.assertTrue(self.source_scanner.accepts_file('test.cpp'))
        self.assertTrue(self.source_scanner.accepts_file('test.cxx'))
        self.assertTrue(self.source_scanner.accepts_file('test.hxx'))
        self.assertTrue(self.source_scanner.accepts_file('test.hpp'))
        self.assertTrue(self.source_scanner.accepts_file('test.ii'))
        self.assertTrue(self.source_scanner.accepts_file('test.i'))
        self.assertTrue(self.source_scanner.accepts_file('test.h'))
        self.assertFalse(self.source_scanner.accepts_file('test.f90'))
        self.assertFalse(self.source_scanner.accepts_file('test.F'))

    def test_scan_file_object_arm64(self):
        report = Report('/root')
        io_object = io.StringIO('xxx')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 0)

        report = Report('/root')
        io_object = io.StringIO('__asm__("")')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 0)

        report = Report('/root')
        io_object = io.StringIO('__asm__("") \\')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 0)

        report = Report('/root')
        io_object = io.StringIO('__asm__ __volatile__( "" : : : "memory" )')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)

        report = Report('/root')
        io_object = io.StringIO('_otherarch_intrinsic_xyz(123)')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)

        report = Report('/root')
        io_object = io.StringIO('#pragma simd foo')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)
        self.assertEqual(report.issues[0].issue_type, ReportItem.PRAGMA)

        report = Report('/root')
        io_object = io.StringIO('#ifndef IMPALA_UTIL_SSE_UTIL_H\n#error "Do not compile with -msse4.1 or higher."')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)
        self.assertEqual(report.issues[0].issue_type, ReportItem.PREPROCESSOR_ERROR)

        report = Report('/root')
        io_object = io.StringIO('#ifdef __GNUC__')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)
        self.assertEqual(report.issues[0].issue_type, ReportItem.COMPILER_SPECIFIC)

        report = Report('/root')
        io_object = io.StringIO('const __m256i m = _mm256_set1_epi32(0x61eaf8e9);')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)
        self.assertEqual(report.issues[0].issue_type, ReportItem.INTRINSIC)

        report = Report('/root')
        io_object = io.StringIO('zmm0 = _mm512_loadu_si512((const void *)src);')
        self.source_scanner.scan_file_object('test.cpp',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)
        self.assertEqual(report.issues[0].issue_type, ReportItem.INTRINSIC)

        report = Report('/root')
        io_object = io.StringIO('zmm0 = _mm_sign_epi32((const void *)src);')
        self.source_scanner.scan_file_object('test.cpp',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)
        self.assertEqual(report.issues[0].issue_type, ReportItem.INTRINSIC)

        report = Report('/root')
        self.source_scanner.scan_file('test.c',
                                      report)
        self.assertEqual(len(report.errors), 1)

        report = Report('/root')
        io_object = io.StringIO('#define')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)

        report = Report('/root')
        io_object = io.StringIO('#if')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)

        report = Report('/root')
        io_object = io.StringIO('#elif')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)

        report = Report('/root')
        io_object = io.StringIO('#ifdef')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)

        report = Report('/root')
        io_object = io.StringIO('#ifndef')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)

    def test_comments_are_ignored(self):
        report = Report('/root')
        io_object = io.StringIO('// __asm__("mov r0, r1")')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 0)

        report = Report('/root')
        io_object = io.StringIO('/*\n__asm__("mov r0, r1")\n*/')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 0)

    def test_function_name(self):
        report = Report('/root')
        io_object = io.StringIO('void func(void) {\n__asm__ __volatile__( "" : : : "memory" );}')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)

    def test_macro_name(self):
        report = Report('/root')
        io_object = io.StringIO('#define MACRO __asm__("" : : : "memory" )')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)

    def test_no_equivalent_inline_asm_single_file(self):
        report = Report('/root')
        self.source_scanner.initialize_report(report)
        io_object = io.StringIO('__asm__("mov r0, r1"')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.source_scanner.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

    def test_equivalent_inline_asm_function_outline(self):
        report = Report('/root')
        self.source_scanner.initialize_report(report)
        io_object = io.StringIO('#if defined(__otherarch__)\nvoid func() {\n__asm__("mov r0, r1");\n}\n#elif defined(__aarch64__)\nvoid func() {\n__asm__("mov r0, r1");\n}\n#endif')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.source_scanner.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

    def test_equivalent_inline_asm_function_inline(self):
        report = Report('/root')
        self.source_scanner.initialize_report(report)
        io_object = io.StringIO('void func() {\n#if defined(__otherarch__)\n__asm__("mov r0, r1");\n#elif defined(__aarch64__)\n__asm__("mov r0, r1");\n#endif\n}')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.source_scanner.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

    def test_no_equivalent_inline_asm_function_outline(self):
        report = Report('/root')
        self.source_scanner.initialize_report(report)
        io_object = io.StringIO('#if defined(__otherarch__)\nvoid func() {\n__asm__("mov r0, r1");\n}\n#elif defined(__aarch64__)\nvoid func() {\nfoo\n}\n#endif')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.source_scanner.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

    def test_no_equivalent_inline_asm_function_inline(self):
        report = Report('/root')
        self.source_scanner.initialize_report(report)
        io_object = io.StringIO('void func() {\n#if defined(__otherarch__)\n__asm__("mov r0, r1");\n#elif defined(__aarch64__)\nfoo\n#endif\n}')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.source_scanner.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

    def test_equivalent_intrinsic_function_outline(self):
        report = Report('/root')
        self.source_scanner.initialize_report(report)
        io_object = io.StringIO('#if defined(__otherarch__)\nvoid func() {\n_otherarch_intrinsic_xyz(123);\n}\n#elif defined(__aarch64__)\nvoid func() {\n_arm_intrinsic(123);\n}\n#endif')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.source_scanner.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

    def test_equivalent_intrinsic_function_inline(self):
        report = Report('/root')
        self.source_scanner.initialize_report(report)
        io_object = io.StringIO('void func() {\n#if defined(__otherarch__)\n_otherarch_intrinsic_xyz(123);\n#elif defined(__aarch64__)\n_arm_intrinsic(123);\n#endif\n}')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.source_scanner.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

    def test_no_equivalent_intrinsic_function_outline(self):
        report = Report('/root')
        self.source_scanner.initialize_report(report)
        io_object = io.StringIO('#if defined(__otherarch__)\nvoid func() {\n_otherarch_intrinsic_xyz(123);\n}\n#elif defined(__aarch64__)\nvoid func() {\nfoo\n}\n#endif')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.source_scanner.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

    def test_no_equivalent_intrinsic_function_inline(self):
        report = Report('/root')
        self.source_scanner.initialize_report(report)
        io_object = io.StringIO('void func() {\n#if defined(__otherarch__)\n_otherarch_intrinsic_xyz(123));\n#elif defined(__aarch64__)\nfoo\n#endif\n}')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.source_scanner.finalize_report(report)
        self.assertEqual(len(report.issues), 0)

    def test_scan_tree(self):
        source_scanner = Scanner()
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ofp:
            ofp.write("test")
            fname = ofp.name
            ofp.close()

        report = Report('/root')
        self.source_scanner.scan_file(fname,
                                      report)

        source_scanner.initialize_report(report)
        self.source_scanner.scan_tree('../test_file/pangu2/benchmark',
                                      report)
        source_scanner.finalize_report(report)
        self.assertEqual(len(report.errors), 0)

    def test_accepts_file_sw64(self):
        self.source_scanner = Sw64SourceScanner(output_format=ReportOutputFormat.HTML, arch='sw64')
        self.assertFalse(self.source_scanner.accepts_file('test'))
        self.assertTrue(self.source_scanner.accepts_file('test.c'))
        self.assertTrue(self.source_scanner.accepts_file('test.cc'))
        self.assertTrue(self.source_scanner.accepts_file('test.CC'))
        self.assertTrue(self.source_scanner.accepts_file('test.cpp'))
        self.assertTrue(self.source_scanner.accepts_file('test.cxx'))
        self.assertTrue(self.source_scanner.accepts_file('test.hxx'))
        self.assertTrue(self.source_scanner.accepts_file('test.hpp'))
        self.assertTrue(self.source_scanner.accepts_file('test.ii'))
        self.assertTrue(self.source_scanner.accepts_file('test.i'))
        self.assertTrue(self.source_scanner.accepts_file('test.h'))
        self.assertFalse(self.source_scanner.accepts_file('test.f90'))
        self.assertFalse(self.source_scanner.accepts_file('test.F'))

    def test_scan_file_object_sw64(self):
        self.source_scanner = Sw64SourceScanner(output_format=ReportOutputFormat.HTML, arch='sw64')

        report = Report('/root')
        io_object = io.StringIO('xxx')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 0)

        report = Report('/root')
        io_object = io.StringIO('const __m128i result = _mm_shuffle_epi8(data, vecmask[desc][0]);')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)

        report = Report('/root')
        io_object = io.StringIO('__asm__ __volatile__(LOCK "addl %1,%0"')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)

        report = Report('/root')
        io_object = io.StringIO('id(void) { __asm__("");')
        self.source_scanner.scan_file_object('test.c',
                                             io_object,
                                             report)
        self.assertEqual(len(report.issues), 1)


if __name__ == '__main__':
    unittest.main()
