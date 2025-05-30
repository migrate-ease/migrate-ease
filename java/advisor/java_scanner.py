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
import locale
import time

from common.json_report import JsonReport
from common.report import Report
from common.scanner import BaseScanner
from common.checkpoint import load_checkpoints

class JavaScanner(BaseScanner):
    JAVA = "java"
    POM = 'pom'
    JAR = 'jar'

    FILE_SUMMARY = {
        JAVA: {
            "fileName": "java",
            "loc": 0,
            "count": 0
        },
        POM: {
            "fileName": "POM",
            "loc": 0,
            "count": 0
        },
        JAR: {
            "fileName": "Jar",
            "loc": 0,
            "count": 0
        }
    }

    checkpoints_content = {}

    def load_checkpoints(self):
        env_language = locale.getdefaultlocale()[0]
        language = 'zh_CN' if env_language.startswith('zh_') else 'en_US'
        current_path = os.path.abspath(os.path.dirname(__file__))
        check_points_yml = os.path.abspath(current_path + './../db/' + language + '/check_points.yaml')

        start_time = time.time()
        self.checkpoints_content = load_checkpoints(check_points_yml)
        end_time = time.time()
        print('[Java] Loading of check_points.yaml took %f seconds.' % (end_time - start_time))


Report.SCANNER = JavaScanner
JsonReport.lang = 'java'
