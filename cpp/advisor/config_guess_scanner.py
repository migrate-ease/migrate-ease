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


class ConfigGuessScanner(CppScanner):

    """
    Scanner that scans config.guess files for aarch64 support.
    """

    TARGET_ARCH_RE = re.compile(r'(aarch64|arm64).*:Linux')

    def __init__(self, output_format, march):
        self.output_format = output_format
        self.march = march

    def accepts_file(self, filename):

        if os.path.basename(filename).lower() in ['config.guess']:
            return True

        return False
