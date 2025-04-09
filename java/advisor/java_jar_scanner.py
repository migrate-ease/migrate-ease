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
import shutil
import zipfile
import magic
import subprocess
from collections import defaultdict

from common.localization import _
from common.arch_strings import AARCH64_ARCHS
from common.report_factory import ReportOutputFormat

from .java_scanner import JavaScanner
from .java_jar_issue import JavaJarIssue


class JavaJarScanner(JavaScanner):
    JAVA_JAR_EXTENSIONS = ['.jar', '.war']
    JAVA_DYNAMIC_LINK_LIBRARY_EXTENSIONS = ['.so', '.dll', '.dylib', '.jnilib']
    JAVA_STATIC_LINK_LIBRARY_EXTENSIONS = ['.a', '.o']

    ELF_RE = re.compile(r'ELF 64-bit.*, ARM aarch64,.*')
    LIBNAME_RE = re.compile(r'^(.*?)-(linux|osx|windows|win)(32|64)?(-\w+)?.*$')

    def __init__(self, output_format, arch, march):
        self.output_format = output_format
        self.arch = arch
        self.march = march

        self.with_highlights = bool(
            output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)

    def accepts_file(self, filename):

        _, ext = os.path.splitext(filename)
        return ext.lower() in self.__class__.JAVA_JAR_EXTENSIONS

    def scan_file_object(self, filename, file_obj, report):

        self.FILE_SUMMARY[self.JAR]['count'] += 1

        issues = []
        lines = {}

        # make sure it is jar or war (zip)
        pkg_type = magic.from_file(filename).lower().split(' ')

        if "zip" in pkg_type or "(jar)" in pkg_type:
            # decompress
            decompress_path = filename[:filename.rfind('.')]
            if not os.path.exists(decompress_path):
                decompress_command = "mkdir {} && unzip -o {} -d {} > /dev/null 2>&1" \
                    .format(decompress_path, filename, decompress_path)
            else:
                decompress_command = "rm -rf {} && mkdir {} && unzip -o {} -d {} > /dev/null 2>&1" \
                    .format(decompress_path, decompress_path, filename, decompress_path)

            subprocess.call(decompress_command, shell=True)

            # search for libraries
            extensions = self.__class__.JAVA_DYNAMIC_LINK_LIBRARY_EXTENSIONS + self.__class__.JAVA_STATIC_LINK_LIBRARY_EXTENSIONS
            libs_list_dict = defaultdict(list)
            for root, dirs, files in os.walk(decompress_path):
                for file in files:
                    if file.endswith(tuple(extensions)):
                        libname = os.path.splitext(file)[0]
                        # on unix system we usually see libxyz.* while on windows
                        # it may be xyz.dll. So remove the 'lib' prefix to put all
                        # related libs (OS/arch) in one group
                        if libname.startswith('lib'):
                            libname = libname[3:]

                        matched = re.match(self.__class__.LIBNAME_RE, libname)
                        # group lib files by the name
                        if matched:
                            # library for multiarch/os is reflected in its name
                            # example: librocksdbjni-<os>-<arch>.so in rocksdbjni-7.9.2.jar
                            libs_list_dict[matched.group(1)].append(os.path.join(root, file))
                        else:
                            # library for multiarch/os is reflected by path
                            # example: org/xerial/snappy/native/<os>/<arch>/libsnappyjava.so in snappy-java-1.1.8.4.jar
                            libs_list_dict[libname].append(os.path.join(root, file))

            # now iterate libs to find if this lib provides Linux/aarch64 version
            lib_idx = 0
            for this_lib in libs_list_dict:
                support_target_arch = False
                for f in libs_list_dict[this_lib]:
                    info = magic.from_file(f)
                    found = re.match(self.__class__.ELF_RE, info)
                    if found:
                        # aarch64/linux version is found, mark this lib as "compatible"
                        support_target_arch = True
                        break

                if support_target_arch == False:
                    exist_libs = '\n\t'.join(libs_list_dict[this_lib])
                    lines[lib_idx] = _("No native lib [%s] for aarch64. Existing libs are:\n\t%s") % (this_lib, exist_libs)
                    issues.append(JavaJarIssue(filename=filename,
                                                 arch=self.arch,
                                                 lineno=0,
                                                 checkpoint=None))
                    lib_idx += 1
            # remove temporary dir for jar
            shutil.rmtree(decompress_path)

        else:
            print("Malformat JAR package, pkg_path: {}".format(filename))
            return False

        for issue, line in zip(issues, lines):
            issue.set_code_snippet(lines[line])
            report.add_issue(issue)

    def finalize_report(self, report):
        pass
