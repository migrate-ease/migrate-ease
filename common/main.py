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
import git

from common.arch_strings import *
from common.issue_type_config import IssueTypeConfig
from common.localization import _
from common.os_strings import *
from common.report_factory import ReportFactory, ReportOutputFormat


# Define mappings for vendors, instance types, and their respective ISAs
PLATFORM_CONFIG = {
    "AWS": {
        "Graviton": ARMV8_0,  # Example: Graviton uses Armv8-A
    },
    "GCP": {
        "C4A": ARMV9_0,  # C4A uses Armv9-A
        "N4A": ARMV9_2,  # N4A uses Armv9.2-A
    }
}

SUPPORTED_VENDORS = list(PLATFORM_CONFIG.keys())

def get_supported_instance_types(vendor):
    return list(PLATFORM_CONFIG.get(vendor, {}).keys())

def get_isa_for_instance_type(vendor, instance_type):
    return PLATFORM_CONFIG.get(vendor, {}).get(instance_type)


def init_main(project, summary, version, ISSUE_TYPES):
    epilog = _('Target ISA Type:') + '\n' + \
             textwrap.fill(('%s' % (','.join(SUPPORTED_MARCH))),
                           initial_indent='  ',
                           subsequent_indent='  ') + '\n\n' + \
             _('Supported Vendors:') + '\n' + \
             textwrap.fill(('%s' % (','.join(SUPPORTED_VENDORS))),
                           initial_indent='  ',
                           subsequent_indent='  ') + '\n\n' + \
             _('Supported Instance Types per Vendor:') + '\n' + \
             textwrap.fill(('%s' % ('; '.join([f'{vendor}: {",".join(get_supported_instance_types(vendor))}' for vendor in SUPPORTED_VENDORS]))),
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
                        help=_('git repository branch.'),
                        default=None)

    parser.add_argument('--commit',
                        help=_('git repository code commit id (default: HEAD).'),
                        default=None)

    parser.add_argument('--march',
                        help=_('the target processor architecture (default: %s).') % DEFAULT_ARCH,
                        default=DEFAULT_ARCH)

    parser.add_argument('--vendor',
                        help=_('the cloud vendor (e.g., GCP, AWS).'),
                        default=None)

    parser.add_argument('--instance-type',
                        help=_('the instance type (e.g., C4A, N4A, Graviton).'),
                        default=None)

    parser.add_argument('--target-os',
                        help=_(
                            'target operating system (default: %s), supported OS (%s).') % (DEFAULT_OS, SUPPORTED_OS),
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
    if not args.march in SUPPORTED_MARCH:
        print(_('unknown/unsupported processor archtecture: %s') % args.march,
              file=sys.stderr)
        print(_('supported architectures: %s') % SUPPORTED_MARCH, file=sys.stderr)
        sys.exit(1)

    if args.vendor:
        if args.vendor not in SUPPORTED_VENDORS:
            print(_('unknown/unsupported vendor: %s') % args.vendor,
                  file=sys.stderr)
            print(_('supported vendors: %s') % SUPPORTED_VENDORS, file=sys.stderr)
            sys.exit(1)

    if args.instance_type:
        if not args.vendor:
            print(_('--instance-type requires --vendor to be specified.'), file=sys.stderr)
            sys.exit(1)
        supported_instance_types = get_supported_instance_types(args.vendor)
        if args.instance_type not in supported_instance_types:
            print(_('unknown/unsupported instance type: %s for vendor %s') % (args.instance_type, args.vendor),
                  file=sys.stderr)
            print(_('supported instance types for %s: %s') % (args.vendor, supported_instance_types), file=sys.stderr)
            sys.exit(1)
        
        derived_march = get_isa_for_instance_type(args.vendor, args.instance_type)
        if derived_march:
            if args.march != DEFAULT_ARCH and args.march != derived_march:
                print(_('specified --march %s conflicts with derived ISA %s from --vendor %s and --instance-type %s') %
                      (args.march, derived_march, args.vendor, args.instance_type), file=sys.stderr)
                sys.exit(1)
            elif args.march == DEFAULT_ARCH:
                args.march = derived_march

    if args.target_os not in SUPPORTED_OS:
        print(_('OS "%s" is not supported.\nSupported OS: %s') % (args.target_os, SUPPORTED_OS),
              file=sys.stderr)
        sys.exit(1)

    if not args.git_repo:
        # For git repo scan, the root directory will be created by clone_git_repo
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

def clone_git_repo(url, branch, commit, dest):
    if os.path.exists(dest):
        if len(os.listdir(dest)) != 0:
            print(f"destination path '{dest}' already exists and is not an empty directory. Skip clone")
            return

    # Clone the repository
    os.makedirs(dest, exist_ok=True)
    try:
        repo = git.Repo.clone_from(url, dest, branch=branch)
        if branch:
            print(f"Successfully cloned {branch} from {url} to {dest}.")
        else:
            print(f"Successfully cloned {url} to {dest}.")

        if commit:
            repo.git.checkout(commit)
    except Exception as e:
        raise Exception(f"{e}")