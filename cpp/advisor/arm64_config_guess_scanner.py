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

import re

from .config_guess_issue import ConfigGuessIssue
from .config_guess_scanner import ConfigGuessScanner


class Arm64ConfigGuessScanner(ConfigGuessScanner):

    """
    Scanner that scans config.guess files for aarch64 support.
    """

    TARGET_ARCH_RE = re.compile(r'(aarch64|arm64).*:Linux')

    def __init__(self, output_format, march):
        self.output_format = output_format
        self.march = march

    def scan_file_object(self, filename, file_obj, report):

        _lines = file_obj.readlines()
        self.FILE_SUMMARY[self.AUTOCONF]['count'] += 1
        self.FILE_SUMMARY[self.AUTOCONF]['loc'] += len(_lines)

        for line in _lines:
            match = Arm64ConfigGuessScanner.TARGET_ARCH_RE.search(line)

            if match:
                break

        # no match found.
        else:
            report.add_issue(ConfigGuessIssue(filename=filename,
                                              remark="autoconf config.guess needs updating to recognize aarch64 architecture"))
