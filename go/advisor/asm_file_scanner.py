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
import time

from common.arch_strings import SUPPORTED_MARCH
from common.checkpoint import Checkpoint, init_checkpoints
from common.continuation_parser import ContinuationParser
from common.find_port import find_matching_line_num
from common.report_factory import ReportOutputFormat

from .asm_issue import AsmIssue
from .go_scanner import GoScanner
from .golang_asm_strings import GOLANG_ASM_AARCH64, GOLANG_ASM_NON_AARCH64, GOLANG_ASM_ALL_ARCHS


class AsmFileScanner(GoScanner):
    """
    Scanner that scans .s source files for potential porting issues
    """

    PY_SOURCE_EXTENSIONS = ['.s']
    AARCH64_NAME_RE = re.compile(r'.*(%s).*' % '|'.join([(r'%s' % x) for x in GOLANG_ASM_AARCH64]))
    NON_AARCH64_NAME_RE = re.compile(r'.*(%s).*' % '|'.join([(r'%s' % x) for x in GOLANG_ASM_NON_AARCH64]))
    aarch64_prefix = 'arm64'

    def __init__(self, output_format, march):
        self.output_format = output_format
        self.march = march

        self.with_highlights = bool(
            self.output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)

    def load_checkpoints(self):
        super().load_checkpoints()

        start_time = time.time()

        self.AARCH64_INCOMPATIBLE_PLAN9_GOLANG_INTRINSICS = init_checkpoints(
            self.checkpoints_content['PLAN9_GOLANG_X86']
        )

        end_time = time.time()

        print('[Go] Initialization of checkpoints took %f seconds.' % (end_time - start_time))

    def accepts_file(self, filename):

        _, ext = os.path.splitext(filename)
        return ext.lower() in self.__class__.PY_SOURCE_EXTENSIONS

    def scan_file_object(self, filename, file_obj, report):

        _lines = file_obj.readlines()
        _, ext = os.path.splitext(filename)

        if ext.lower() in self.__class__.PY_SOURCE_EXTENSIONS:
            self.FILE_SUMMARY[self.S]['count'] += 1
            self.FILE_SUMMARY[self.S]['loc'] += len(_lines)

        issues = []  # type: List[Issue]
        lines = {}
        # Go assembly file naming usually follows any of the following patterns:
        #   *_<goos>.s or *_<goarch>.s or *_<goos>_<goarch>.s
        #   where <goarch> is the architecture suffix.
        # See the go docs for more details: https://pkg.go.dev/cmd/go#hdr-Build_constraints
        if self.march in SUPPORTED_MARCH:
            directory, fname = os.path.split(filename)
            if '_' in fname:
                # If the file name contains a suffix, check whether it is an architecture suffix,
                # and verify if it matches the target architecture.
                base_name = os.path.splitext(fname)[0]
                # The file extension may be .s or .S, so we extract it separately.
                ext_name = os.path.splitext(fname)[1]
                fname_prefix = base_name.rsplit('_', 1)[0]
                arch_suffix = base_name.rsplit('_', 1)[1]
                match_other_archs = self.__class__.NON_AARCH64_NAME_RE.search(arch_suffix)
                match_aarch64 = self.__class__.AARCH64_NAME_RE.search(arch_suffix)

                if match_aarch64:
                    # Detect '_arm64' suffix in file name to confirm it matches the target architecture.
                    issues = []
                elif match_other_archs:
                    # If the file does not match the aarch64 architecture, attempt to find a corresponding
                    # "_arm64.s" version.
                    expected_aarch64_file = f"{fname_prefix}_{self.aarch64_prefix}{ext_name}"
                    aarch64_file_path = os.path.join(directory, expected_aarch64_file)
                    if not os.path.exists(aarch64_file_path):
                        lines[0] = "File: " + filename + " is not supported on target processor architecture: " + self.march
                        issues.append(AsmIssue(filename=filename,
                                   march=self.march,
                                   lineno=0,
                                   checkpoint=None,
                                   description=lines[0]))
                else:
                    # If the suffix is not a known architecture suffix or does not have a architecture suffix, manual check is required.
                    lines[0] = "File: " + filename + " is not implemented for known architectures: " + ", ".join(GOLANG_ASM_ALL_ARCHS) + \
                                "\ncheck that it is compatible with the target architecture."
                    issues.append(AsmIssue(filename=filename,
                                march=self.march,
                                lineno=0,
                                checkpoint=None,
                                description=lines[0]))
            else:
                # If the file has no suffix, it may be a generic file, and needs to be checked manually.
                lines[0] = "File: " + filename + " may be a generic file, \n" + \
                            "check that it is compatible with the target architecture."
                issues.append(AsmIssue(filename=filename,
                            march=self.march,
                            lineno=0,
                            checkpoint=None,
                            description=lines[0]))

        #  to extract code snippets
        for issue in issues:
            issue.set_code_snippet(issue.get_code_snippets(lines, with_highlights=self.with_highlights))
            report.add_issue(issue)
