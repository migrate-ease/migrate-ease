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
from common.localization import _
from common.issue import BaseReportItem
from common.report import Report


class ReportItem(BaseReportItem):
    JAVA_JAR = {'type': 'JarIssue', 'des': _('JAR package does not support target arch. Need to rebuild or upgrade.')}
    JAVA_POM = {'type': 'PomIssue', 'des': _('Pom imports java artifact that does not support target arch.')}
    JAVA_SOURCE = {'type': 'JavaSourceIssue', 'des': _('Java source file contains native call that may need modify/rebuild for target arch.')}

    TYPES = BaseReportItem.TYPES + [
        JAVA_JAR,
        JAVA_POM,
        JAVA_SOURCE
        ]

Report.REPORT_ITEM = ReportItem
