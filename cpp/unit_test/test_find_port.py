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

from advisor.find_port import *


class TestFindPort(unittest.TestCase):

    def test_port_filenames(self):

        self.assertListEqual(port_filenames("filename"), [])

        self.assertListEqual(port_filenames("otherarch"),
                             ['aarch64', 'arm64', 'arm', 'neon', 'sve'])

        self.assertListEqual(port_filenames("arm"),
                             ['arm'])

        self.assertListEqual(port_filenames("source-otherarch.c"),
                             ['source-aarch64.c', 'source-arm64.c',
                              'source-arm.c', 'source-neon.c',
                              'source-sve.c'])

    def test_find_port_dir(self):

        self.assertEqual(find_port_dir('/foo/otherarch', ['/foo/otherarch', '/foo/aarch64']), '/foo/aarch64')
        self.assertEqual(find_port_dir('/foo/otherarch', ['/xxx', '/xxx']), None)

    def test_is_arch_specific_file_name(self):
        self.assertEqual(is_arch_specific_file_name('/foo/aarch64/source.c', "arm64"), True)
        self.assertEqual(is_arch_specific_file_name('/foo/sw64/source.c', "sw64"), True)
        self.assertEqual(is_arch_specific_file_name('/foo/xxx/source.c', "sw64"), False)
        try:
            is_arch_specific_file_name('/foo/xxx/source.c', "xx")
        except RuntimeError as e:
            print(e.args)

    def test_find_matching_line_num(self):
        self.assertEqual(find_matching_line_num({1: "aaa", 2: "bbb"}, 1, None), 1)
        self.assertEqual(find_matching_line_num({1: "aaa", 2: "_mm_shuffle_epi8(", 3: "bbb"}, 3, "_mm_shuffle_epi8"), 2)

    def test_find_port_file(self):

        self.assertEqual(find_port_file('/foo/source-otherarch.c',
                                        ['/foo/source-otherarch.c',
                                         '/foo/source-aarch64.c']),
                         '/foo/source-aarch64.c')

        self.assertEqual(find_port_file('/foo/otherarch/source.c',
                                        ['/foo/otherarch/source.c',
                                         '/foo/aarch64/source.c']),
                         '/foo/aarch64/source.c')

        self.assertEqual(find_port_file('/foo/otherarch/source.c',
                                        ['/foo/otherarch/source.c',
                                         '/foo/aarch64/source.c'],
                                        '/foo/otherarch'),
                         # '/foo/aarch64/source.c')
                         None)


if __name__ == '__main__':
    unittest.main()
