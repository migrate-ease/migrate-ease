"""
Copyright 2017-2025 Arm Ltd.

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
from collections import defaultdict

from common.localization import _
from common.arch_strings import AARCH64_ARCHS
from common.report_factory import ReportOutputFormat

from .java_scanner import JavaScanner
from .java_source_issue import JavaSourceIssue


class JavaSourceScanner(JavaScanner):

    JAVA_SOURCE_EXTENSION = ['.java']

    def __init__(self, output_format, arch, march):
        self.output_format = output_format
        self.arch = arch
        self.march = march

        self.with_highlights = bool(
            output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)

    def accepts_file(self, filename):

        _, ext = os.path.splitext(filename)
        return ext.lower() in self.__class__.JAVA_SOURCE_EXTENSION

    def scan_file_object(self, filename, file_obj, report):

        self.FILE_SUMMARY[self.JAVA]['count'] += 1

        # Patterns to detect native-related code
        native_patterns = [
            r'\bnative\s',  # Matches the 'native' keyword in method declarations
            r'System\.loadLibrary\s*\(',  # Matches System.loadLibrary(...)
            r'System\.load\s*\(',  # Matches System.load(...)
            r'import\s+java\.nio\.\*',  # Matches 'import java.nio.*'
            r'import\s+sun\.misc\.\*',  # Matches 'import sun.misc.*'
            r'\bJNI(Env|EXPORT|CALL)\b',  # Matches JNI (e.g., JNIEnv)
            r'Java_com_[a-zA-Z0-9_]*_[a-zA-Z0-9_]*',  # Matches JNI-style method names
        ]

        # Compile the regex patterns
        compiled_patterns = [re.compile(pattern) for pattern in native_patterns]
        issues = []
        lines = {}

        try:
            lines = file_obj.readlines()
            self.FILE_SUMMARY[self.JAVA]['loc'] += len(lines)

            # Find all comments with line numbers
            comment_loc = []
            for line_number, line in enumerate(lines, start=0):
                # Check for block comments
                block_comment_start = re.search(r'/\*', line)
                block_comment_end = re.search(r'\*/', line)
                if block_comment_start:
                    comment_loc.append(line_number)
                    if block_comment_end:
                        continue  # End of block comment found in the same line

                    # Continue to find the end of the block comment
                    for subsequent_line in lines[line_number:]:
                        line_number += 1
                        comment_loc.append(line_number)
                        if re.search(r'\*/', subsequent_line):
                            break

                # Check for inline comments
                inline_comment = re.search(r'//.*', line)
                if inline_comment and not line_number in comment_loc:
                    comment_index = line.strip().index('//')
                    # inline comment may appear after code, if yes, skip it
                    if comment_index == 0:
                        comment_loc.append(line_number)

            # Check for native patterns
            for line_number, line in enumerate(lines, start=0):
                # Check each line for native-related patterns
                for pattern in compiled_patterns:
                    if pattern.search(line) and not line_number in comment_loc:
                        issues.append(JavaSourceIssue(filename,
                                            lineno=line_number,
                                            arch=self.arch,
                                            checkpoint=pattern.pattern)
                                            )
                        break  # Stop checking other patterns for this line

        except Exception as e:
            print(f"Error reading file {filename}: {e}")

        for issue in issues:
            issue.set_code_snippet(issue.get_code_snippets(lines=lines, with_highlights=self.with_highlights))
            report.add_issue(issue)

    def finalize_report(self, report):
        pass
