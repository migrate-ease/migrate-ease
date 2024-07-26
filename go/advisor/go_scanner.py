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

from common.json_report import JsonReport
from common.report import Report
from common.scanner import BaseScanner


class GoScanner(BaseScanner):
    GO = 'go'
    GOLIBS = 'libs'
    S = 's'

    FILE_SUMMARY = {
        GO: {
            "fileName": "Golang 文件",
            "loc": 0,
            "count": 0
        },
        GOLIBS: {
            "fileName": "Lib 文件",
            "loc": 0,
            "count": 0
        },
        S: {
            "fileName": "Asm 文件",
            "loc": 0,
            "count": 0
        }

    }


Report.SCANNER = GoScanner
JsonReport.lang = 'go'
