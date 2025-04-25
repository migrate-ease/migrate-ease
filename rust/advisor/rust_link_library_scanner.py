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
import os
import re

from common.arch_strings import *
from common.binary_tools import *
from common.report_factory import ReportOutputFormat
from .rust_link_library_issue import RustLinkLibraryIssue
from .rust_scanner import RustScanner


class RustLinkLibraryScanner(RustScanner):
    RUST_DYNAMIC_LINK_LIBRARY_EXTENSIONS = ['.so', '.dll', '.dylib']

    RUST_STATIC_LINK_LIBRARY_EXTENSIONS = ['.a', '.o']

    EM_AARCH64 = ['EM_AARCH64', 'EM_ARM']

    SO_RE = re.compile(r'.*[.](so)[.]?')

    def __init__(self, output_format, arch, march):
        self.output_format = output_format
        self.arch = arch
        self.march = march

        self.with_highlights = bool(
            output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)

    def accepts_file(self, filename):

        match = self.__class__.SO_RE.search(filename)
        is_obj = is_library(filename)

        # Only check object file
        if is_obj:
            if match:
                ext = '.so'
            else:
                _, ext = os.path.splitext(filename)
            return ext.lower() in [
                *self.__class__.RUST_DYNAMIC_LINK_LIBRARY_EXTENSIONS,
                *self.__class__.RUST_STATIC_LINK_LIBRARY_EXTENSIONS
            ]
        else:
            return False

    def scan_file_arch(self, match, file_arch):

        if self.arch in AARCH64_ARCHS:
            if file_arch not in self.__class__.EM_AARCH64:
                match = True

        return match

    def scan_file_object(self, filename, file_obj, report):

        self.FILE_SUMMARY[self.RUSTLIBS]['count'] += 1

        issues = []
        lines = {}
        match = False
        lib_idx = 0

        _, ext = os.path.splitext(filename)

        # dynamic lib and .o file
        if ext != '.a':

            machine_code = get_elf_machine_code(filename)
            if not machine_code:
                file_arch = get_target_machin(filename)
            else:
                file_arch = get_file_arch(machine_code)

            lines[lib_idx] = "The machine type of the link library '%s' is %s" % (filename, file_arch)

            match = self.scan_file_arch(match, file_arch)
            if match:
                issues.append(RustLinkLibraryIssue(filename=filename,
                                                   arch=self.arch,
                                                   lineno=0,
                                                   checkpoint=None))

        # .a file
        else:

            machine_codes = get_machine_of_static_lib(filename)
            if not machine_codes:
                return
            for key in machine_codes:

                file_arch = get_file_arch(machine_codes[key])

                lines[lib_idx] = "the elf machine type of the link library '%s' is %s" % (filename, file_arch)

                match = self.scan_file_arch(match, file_arch)
                if match:
                    issues.append(RustLinkLibraryIssue(filename=filename,
                                                       arch=self.arch,
                                                       lineno=0,
                                                       checkpoint=None))
                    break

                match = False

        for issue, line in zip(issues, lines):
            issue.set_code_snippet(lines[line])
            report.add_issue(issue)

    def finalize_report(self, report):
        pass
