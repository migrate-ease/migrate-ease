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
import sys

from common.main import init_main, check, clone_git_repo
from common.arch_strings import *
from common.progress import create_progress_for_scanner
from common.issue import BaseReportItem
from common.report import Report
from common.auto_scanner import AutoScanner
from common.issue_type_config import IssueTypeConfig

from . import __project__, __target__, __summary__, __version__
from .issue_types import ISSUE_TYPES
from .arm64_scanners import Arm64Scanners
from .report_item import PYTHON_REPORT_TYPES


def main():
    parser = init_main(__project__, __summary__, __version__, ISSUE_TYPES)

    args = parser.parse_args()

    report_factory = check(args)
    
    Report.REPORT_ITEM = BaseReportItem
    Report.REPORT_ITEM.TYPES += PYTHON_REPORT_TYPES

    report = report_factory.createReport(args.root,
                                         march=args.march,
                                         target_os=args.target_os,
                                         output=args.output,
                                         output_format=args.output_format,
                                         issue_type_config=args.issue_types,
                                         git_repo=args.git_repo,
                                         branch=args.branch,
                                         commit=args.commit,
                                         quiet=args.quiet,
                                         progress=args.progress)

    issue_type_config_instance = IssueTypeConfig(args.issue_types, ISSUE_TYPES)

    # Check if a git repo is specified
    if args.git_repo:
        # Clone it with given repo, branch or commit
        try:
            clone_git_repo(args.git_repo, args.branch, args.commit, args.root)
        except Exception as e:
            print(f"Error occurred while cloning [{args.git_repo}] : {e}")
            sys.exit(1)

    if args.march in SUPPORTED_MARCH:
        scanners = Arm64Scanners(issue_type_config_instance,
                                 output_format=args.output_format,
                                 march=args.march)

    else:
        raise RuntimeError('no scanner available for target processor architecture %s.' % args.march)

    scanners.initialize_report(report)
    scanner = AutoScanner(scanners)
    scanner.scan_tree(args.root,
                      report,
                      progress_callback=create_progress_for_scanner(__target__) if args.progress else None)

    scanners.finalize_report(report)

    if args.output:
        with open(args.output, 'w') as f:
            report.write(f, report_errors=not args.quiet)
    else:
        report.write(sys.stdout, report_errors=not args.quiet)
