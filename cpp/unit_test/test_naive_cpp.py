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

from advisor.naive_cpp import *


class TestNaiveCpp(unittest.TestCase):
    def setUp(self):
        self.march = 'armv8-a'

    def tearDown(self):
        pass

    def test_parse_line_arch(self):
        try:
            naive_cpp = NaiveCpp(march="unknown_arch")
        except RuntimeError as e:
            print(e.args)

        naive_cpp = NaiveCpp(march=self.march)
        naive_cpp.parse_line('/* a comment */')
        self.assertFalse(naive_cpp.in_arch_specific_code())

        naive_cpp.parse_line('#ifdef __aarch64__')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#else')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())

        naive_cpp.parse_line('#ifdef otherarch')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#else')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#if defined(__aarch64__)')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#else')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#if defined(otherarch)')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#else')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#ifdef __aarch64__')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#ifdef foo')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#ifdef foo')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#ifdef __aarch64__')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#if !defined(__aarch64__)')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#else')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#if !defined(otherarch)')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#else')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        naive_cpp.parse_line('#if __aarch64__')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#else')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#if otherarch')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#else')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#if !__aarch64__')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#else')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#if !otherarch')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#else')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#if  defined ( __aarch64__)')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#if  !  defined ( __aarch64__)')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#else')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#if aarch64')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#elif otherarch')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('asm("")')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())

    def test_in_compiler_specific_code(self):
        naive_cpp = NaiveCpp(march=self.march)
        naive_cpp.parse_line('#ifdef __INTEL_COMPILER\n\tto_words[0] = from_words[0]\n#else')
        self.assertTrue(naive_cpp.in_compiler_specific_code())

        naive_cpp = NaiveCpp(march=self.march)
        naive_cpp.parse_line('#ifdef xxx')
        self.assertFalse(naive_cpp.in_compiler_specific_code())

    def test_parse_line_pragma(self):
        naive_cpp = NaiveCpp(march=self.march)

        result = naive_cpp.parse_line('#pragma simd foo')
        self.assertEqual(result.directive_type,
                         PreprocessorDirective.TYPE_PRAGMA)

    def test_parse_line_error(self):
        naive_cpp = NaiveCpp(march=self.march)

        result = naive_cpp.parse_line('#error foo')
        self.assertEqual(result.directive_type,
                         PreprocessorDirective.TYPE_ERROR)

    def test_parse_line_ifdef_compiler(self):
        naive_cpp = NaiveCpp(arch=self.arch)

        result = naive_cpp.parse_line('#ifdef __GNUC__')
        self.assertEqual(result.directive_type,
                         PreprocessorDirective.TYPE_CONDITIONAL)
        self.assertTrue(result.is_compiler)

    def test_aarch64_re(self):
        match = NaiveCpp.AARCH64_MACROS_RE.match('aarch64')
        self.assertIsNotNone(match)

        match = NaiveCpp.AARCH64_MACROS_RE.match('__aarch64__')
        self.assertIsNotNone(match)

        match = NaiveCpp.AARCH64_MACROS_RE.match('foo')
        self.assertIsNone(match)

    def test_non_aarch64_re(self):
        match = NaiveCpp.NON_AARCH64_MACROS_RE.match('otherarch')
        self.assertIsNotNone(match)

        match = NaiveCpp.NON_AARCH64_MACROS_RE.match('__otherarch__')
        self.assertIsNotNone(match)

        match = NaiveCpp.NON_AARCH64_MACROS_RE.match('foo')
        self.assertIsNone(match)

    def test_compiler_re(self):
        match = NaiveCpp.ALL_COMPILER_MACROS_RE.match('GNUC')
        self.assertIsNotNone(match)

        match = NaiveCpp.ALL_COMPILER_MACROS_RE.match('__GNUC__')
        self.assertIsNotNone(match)

        match = NaiveCpp.ALL_COMPILER_MACROS_RE.match('foo')
        self.assertIsNone(match)

    def test_macro_body(self):
        naive_cpp = NaiveCpp(march=self.march)

        result = naive_cpp.parse_line('#define MACRO BODY')
        self.assertEqual(result.directive_type,
                         PreprocessorDirective.TYPE_DEFINE)
        self.assertEqual(result.macro_name, 'MACRO')
        self.assertEqual(result.body, 'BODY')

        result = naive_cpp.parse_line('#define MACRO(a,b,c) BODY')
        self.assertEqual(result.directive_type,
                         PreprocessorDirective.TYPE_DEFINE)
        self.assertEqual(result.macro_name, 'MACRO(a,b,c)')
        self.assertEqual(result.body, 'BODY')

    def test_parse_line_if_else(self):
        naive_cpp = NaiveCpp(march=self.march)

        naive_cpp.parse_line('/* a comment */')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('#if defined (__otherarch__)')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('/* a comment */')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('#else')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('/* a comment */')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

    def test_parse_line_if_elif_else(self):
        naive_cpp = NaiveCpp(march=self.march)

        naive_cpp.parse_line('/* a comment */')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('#if defined (__otherarch__)')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('/* a comment */')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('#elif defined (__aarch64__)')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('/* a comment */')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('#else')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('/* a comment */')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

    def test_parse_line_if_elif_elif_else(self):
        naive_cpp = NaiveCpp(march=self.march)

        naive_cpp.parse_line('/* a comment */')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('#if defined (__otherarch__)')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('/* a comment */')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('#elif defined (__aarch64__)')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('/* a comment */')
        self.assertTrue(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('#elif defined (__otherarch__)')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('/* a comment */')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertTrue(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('#else')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('/* a comment */')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())

        naive_cpp.parse_line('#endif')
        self.assertFalse(naive_cpp.in_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_specific_code())
        self.assertFalse(naive_cpp.in_other_arch_else_code())


if __name__ == '__main__':
    unittest.main()
