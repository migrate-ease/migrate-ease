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

import argparse
import os
import sys
import textwrap

from common.arch_strings import *
from common.issue_type_config import IssueTypeConfig
from common.localization import _
from common.os_strings import *
from common.report_factory import ReportFactory, ReportOutputFormat


def init_main(project, summary, version, ISSUE_TYPES):
    epilog = _('Target ISA Type:') + '\n' + \
             textwrap.fill(_('%s' % (','.join(AARCH64_ARCHS))),
                           initial_indent='  ',
                           subsequent_indent='  ') + '\n\n' + \
             _('Use:') + '\n' + \
             textwrap.fill(_('--issue-types=+CompilerSpecific to enable reporting of use of compiler-specific macros.'),
                           initial_indent='  ',
                           subsequent_indent='    ') + '\n' + \
             textwrap.fill(_('--issue-types=+CrossCompile to enable reporting of cross-compile specific issues.'),
                           initial_indent='  ',
                           subsequent_indent='    ') + '\n' + \
             textwrap.fill(
                 _('--issue-types=+NoEquivalent to enable reporting of aarch64 ported code that does not use intrinsics inline assembly versus other architectures.'),
                 initial_indent='  ',
                 subsequent_indent='    ') + '\n\n' + \
             _('Available issue types:') + '\n' + \
             textwrap.fill(', '.join(sorted(ISSUE_TYPES.keys())),
                           initial_indent='  ',
                           subsequent_indent='  ')

    parser = argparse.ArgumentParser(
        prog=project,
        description=summary,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('root',
                        metavar='DIRECTORY',
                        help=_('root directory of source tree to scan (default: .).'),
                        default='.')

    parser.add_argument('--git-repo',
                        help=_('git repository address to scan, when present, repo will be cloned to local.'),
                        metavar='REPO',
                        default=None)

    parser.add_argument('--branch',
                        help=_('git repository branch (default: master).'),
                        default=None)

    parser.add_argument('--commit',
                        help=_('git repository code commit id (default: HEAD).'),
                        default=None)

    parser.add_argument('--arch',
                        help=_('target instruction set architecture (default: %s).' % DEFAULT_ARCH),
                        default=DEFAULT_ARCH)

    parser.add_argument('--march',
                        help=_('target microarchitecture name, required when arch is x86 (default: None).'),
                        default=None)

    parser.add_argument('--target-os',
                        help=_(
                            'target operating system (default: %s), supported OS (%s).' % (DEFAULT_OS, SUPPORTED_OS)),
                        metavar='OS',
                        default=DEFAULT_OS)

    parser.add_argument('--output',
                        help=_('report file name.'),
                        default=None)

    parser.add_argument('--output-format',
                        help=_('output format: %s (default: %s).') %
                             (','.join(str(output_format.value) for output_format in ReportOutputFormat),
                              ReportOutputFormat.DEFAULT.value),
                        metavar='FORMAT',
                        default=ReportOutputFormat.DEFAULT.value)

    parser.add_argument('--issue-types',
                        metavar='TYPES',
                        help=_('types of issue that are reported (default: "%s").') % IssueTypeConfig.DEFAULT_FILTER)

    parser.add_argument('--no-progress',
                        action='store_false',
                        help=_('when set, there will be no progress bar.'),
                        dest='progress')

    parser.add_argument('--quiet',
                        action='store_true',
                        help=_('suppress file errors.'),
                        default=False)

    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s ' + version)

    return parser


def check(args):
    if not args.arch in AARCH64_ARCHS:
        print(_('unknown/unsupported arch: %s') % args.arch,
              file=sys.stderr)
        sys.exit(1)

    if args.target_os not in SUPPORTED_OS:
        print(_('OS "%s" is not supported.\nSupported OS: %s' % (args.target_os, SUPPORTED_OS)),
              file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(args.root):
        print(_('%s: directory not found.') % args.root,
              file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir(args.root):
        print(_('%s: not a directory.') % args.root,
              file=sys.stderr)
        sys.exit(1)

    try:
        report_factory = ReportFactory()
        args.output_format = ReportOutputFormat(args.output_format)

        if args.output_format == ReportOutputFormat.AUTO:
            if not args.output:
                args.output_format = ReportOutputFormat.TEXT
            else:
                # Take the output format from the output file extension.
                args.output_format = report_factory.output_format_for_extension(os.path.splitext(args.output)[1][1:])

                if not args.output_format:
                    raise ValueError

        return report_factory
    except ValueError:
        print(_('%s: invalid output format') % args.output_format, file=sys.stderr)
        sys.exit(1)
