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

from .cpp_scanner import CppScanner
from .makefile_scanner import MakefileScanner


class BinaryScanner(CppScanner):

    """
    Scanner that scans binaries.
    """

    def accepts_file(self, filename):

        basename = os.path.basename(filename)

        return basename in MakefileScanner.MAKEFILE_NAMES or \
            basename.lower() in MakefileScanner.MAKEFILE_NAMES_CASE_INSENSITIVE or \
            basename in MakefileScanner.CMAKE_NAMES or \
            basename.split('.')[-1] in MakefileScanner.CMAKE_NAMES
