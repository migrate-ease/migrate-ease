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

import sys

from common.arch_strings import *
from common.auto_scanner import AutoScanner
from common.issue_type_config import IssueTypeConfig
from common.localization import _
from common.main import check, init_main
from common.progress import create_progress_for_scanner
from . import __project__, __summary__, __target__, __version__
from .arm64_scanners import Arm64Scanners
from .issue_types import ISSUE_TYPES


def main():
    parser = init_main(__project__, __summary__, __version__, ISSUE_TYPES)

    parser.add_argument('--target-compiler',
                        help=_(
                            'target compiler(default: %s), supported OS (%s).'
                            % (DEFAULT_COMPILER, SUPPORTED_COMPILERS_ARM)),
                        metavar='COMPILER',
                        default=DEFAULT_COMPILER)

    parser.add_argument('--warning-level',
                        help=_(
                            'warning level (default: %s), supported level (%s).'
                            'indicate the certainty when report a warning,'
                            'L1 ---- only report a warning with great certainty,'
                            'L2 ---- report a warning with less certainty'
                            % ('L1', ['L1', 'L2'])),
                        metavar='LEVEL',
                        default='L1')

    args = parser.parse_args()

    report_factory = check(args)

    report = report_factory.createReport(args.root,
                                         arch=args.arch,
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
    if args.arch == N2_MARCH:
        try:
            if args.target_compiler not in SUPPORTED_COMPILERS_ARM:
                raise ValueError
        except ValueError:
            print(_('%s: invalid compiler for N2') % args.target_compiler, file=sys.stderr)
            sys.exit(1)
        try:
            if args.warning_level not in ['L1', 'L2']:
                raise ValueError
        except ValueError:
            print(_('%s: invalid warning_level for N2') % args.warning_level, file=sys.stderr)
            sys.exit(1)
    if args.arch in AARCH64_ARCHS:
        scanners = Arm64Scanners(issue_type_config_instance,
                                 output_format=args.output_format,
                                 arch=args.arch,
                                 march=args.march,
                                 compiler=args.target_compiler,
                                 warning_level=args.warning_level)

    else:
        raise RuntimeError('no scanner available for arch %s.' % args.arch)

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
