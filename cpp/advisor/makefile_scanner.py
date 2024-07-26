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

import os
import re

from .cpp_scanner import CppScanner


class MakefileScanner(CppScanner):

    """
    Scanner that scans Makefiles.
    """

    MAKEFILE_NAMES = ['Makefile.in', 'Makefile.am']

    CMAKE_NAMES = ['CMakeLists.txt', 'cmake']

    MAKEFILE_NAMES_CASE_INSENSITIVE = ['makefile', 'nmakefile', 'makefile.mk']

    OLD_CRT_RE = re.compile(r'(libcmt[a-z]*\.lib)|(cmt[a-z]*\.lib)', re.IGNORECASE)

    UCRT_RE = re.compile(r'(libucrt[a-z]*\.lib)', re.IGNORECASE)

    TARGET_RE = re.compile(r'^([a-zA-Z()$_0-9./\\]+)\s*:', re.IGNORECASE)

    COMMAND_RE = re.compile(r'^\t(?:([a-zA-Z()$_0-9./\\]+)|"([a-zA-Z()$_0-9./\\ ]+)")(?:$|\s)', re.IGNORECASE)

    ASSIGNMENT_RE = re.compile(r'^([a-zA-Z()$_0-9]+)\s*=\s*(.*)$', re.IGNORECASE)

    def accepts_file(self, filename):

        basename = os.path.basename(filename)

        return basename in self.__class__.MAKEFILE_NAMES or \
            basename.lower() in self.__class__.MAKEFILE_NAMES_CASE_INSENSITIVE or \
            basename in self.__class__.CMAKE_NAMES or \
            basename.split('.')[-1] in self.__class__.CMAKE_NAMES
