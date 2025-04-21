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
import locale
import time

from common.json_report import JsonReport
from common.report import Report
from common.scanner import BaseScanner
from common.checkpoint import load_checkpoints
from .cpp_lib_version_issue import CPPLibVersionIssue


class CppScanner(BaseScanner):
    CPP_LIB_CHECK_VERSION_LIST = ['boost']
    CPP_LIB_VERSION_DICT = {'boost': '106000'}

    CPP_LIB_WHITE_LIST = ['folly', 'asio', 'msgpack']

    CPP_LIB_RECOMMEND_LIST = ['zstd']

    C = 'c'
    CPP = 'cpp'
    ASSEMBLY = 'asm'
    MAKEFILE = 'makefile'
    AUTOCONF = 'config.guess'

    FILE_SUMMARY = {
        C: {
            "fileName": "C",
            "loc": 0,
            "count": 0
        },
        CPP: {
            "fileName": "CPP",
            "loc": 0,
            "count": 0
        },
        MAKEFILE: {
            "fileName": "Makefile",
            "loc": 0,
            "count": 0
        },
        AUTOCONF: {
            "fileName": "Autoconf",
            "loc": 0,
            "count": 0
        },
        ASSEMBLY: {
            "fileName": "Assembly",
            "loc": 0,
            "count": 0
        }
    }

    checkpoints_content = {}

    def load_checkpoints(self):
        env_language = locale.getdefaultlocale()[0]
        language = env_language if env_language is not None else 'en_US'
        current_path = os.path.abspath(os.path.dirname(__file__))
        check_points_yml = os.path.abspath(current_path + './../db/' + language + '/check_points.yaml')

        start_time = time.time()
        self.checkpoints_content = load_checkpoints(check_points_yml)
        end_time = time.time()
        print('[C/C++] Loading of check_points.yaml took %f seconds.' % (end_time - start_time))

    def check_version(self, root, libname, report):

        version_filename = 'version.hpp'
        for dirName, _, fileList in os.walk(root):
            if version_filename not in fileList:
                continue

            path = os.path.join(dirName, version_filename)
            with open(path, 'r') as file:
                for lineno, line in enumerate(file.readlines()):
                    lineno = lineno + 1
                    if line.find('define') > 0 and line.find('_VERSION ') > 0:
                        ver_str = line[line.find('_VERSION ') + 9:line.find(' //')].strip()
                        if ver_str > self.CPP_LIB_VERSION_DICT[libname]:
                            return True
                        else:
                            desc = f'{libname} version should be higher than {self.CPP_LIB_VERSION_DICT[libname]}'
                            report.add_issue(CPPLibVersionIssue(path, lineno, desc))
                            return False
        else:
            return False

    def check_recommend(self, root, libname, report):
        return False

    def scan_tree(self, root, report, progress_callback=None):
        """
        Scans the filesysem tree starting at root for potential porting issues.

        Args:
            root (str): The root of the filesystem tree to scan.
            report (Report): Report to add issues to.
            progress_callback (function): Optional callback called with file names.
        """
        for filename in os.listdir(root):
            if filename in self.CPP_LIB_WHITE_LIST:
                return
            elif filename in self.CPP_LIB_CHECK_VERSION_LIST and \
                    self.check_version(root, filename, report):
                return
            elif filename in self.CPP_LIB_RECOMMEND_LIST \
                    and self.check_recommend(root, filename, report):
                return

        for dirName, _, fileList in os.walk(root):

            fileList.sort()

            for fname in fileList:

                path = os.path.join(dirName, fname)
                if not self._is_vcs_directory(path) and self.accepts_file(path):

                    if progress_callback:
                        progress_callback(path)

                    self.scan_file(path, report)


Report.SCANNER = CppScanner
JsonReport.lang = 'cpp'
