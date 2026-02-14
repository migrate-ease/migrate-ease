import argparse
import functools
import json
import pathlib
import sys
from pathlib import Path
from common.localization import _
from common.arch_strings import SUPPORTED_MARCH


def _check_blacklist(package_name, version, result, file, file_lines):
    version = tuple(version.split('.'))
    msg = None
    if package_name == 'serialport':
        if version <= ('7', '1', '5'):
            msg = _("Please upgrade serialport to version >= 8.0.5")
    elif package_name == 'node-sass':
        if version <= ('6', '0', '7'):
            msg = _("Please upgrade node-sass to version >= 6.0.1")
    elif package_name == 'sass-loader':
        if version <= ('6', '0', '7'):
            msg = _("sass-loader <= 6.0.7 is not supported")
    elif package_name == 'hiredis':
        msg = _("hiredis is deprecated")
    elif package_name == 'puppeteer':
        msg = _("Need manual installation of chromium")
    elif package_name == 'fsevents':
        msg = _("fsevents is not supported")
    elif package_name in ('phantomjs', 'phantomjs-prebuilt'):
        msg = _("f'{package_name} is not supported")
    elif package_name == 'grpc':
        if version < ('1', '24', '10'):
            msg = _("grpc is deprecated. Please use @grpc/grpc-js instead.")

    if msg is not None:
        result['total_issue_count'] += 1
        result['issue_summary']['ArchSpecificLibraryIssue']['count'] += 1

        for lineno, line in enumerate(file_lines):
            if package_name in line:
                break
        else:
            lineno = 0
            line = ''

        result['issues'].append({
            "checkpoint": "",
            "description": msg,
            "filename": str(file),
            "issue_type": {
                "des": _("Incompatible NPM packages"),
                "type": "ArchSpecificLibraryIssue"
            },
            "lineno": lineno,
            "snippet": line
        })


def load_file(func):
    @functools.wraps(func)
    def inner(file: pathlib.Path, result):
        file_name = str(file)
        if file_name not in result['source_files']:
            result['source_files'].append(file_name)

            dir_name = str(file.parent)
            if dir_name not in result['source_dirs']:
                result['source_dirs'].append(dir_name)
        try:
            fs = file.read_text()
            lines = fs.split('\n')
            cont = json.loads(fs)

            result['file_summary']['npm']['count'] += 1
            result['file_summary']['npm']['loc'] += len(lines)
        except json.JSONDecodeError:
            # todo: parse error
            return
        return func(cont, result, str(file), lines)

    return inner


@load_file
def handle_package_json(cont, result, file, file_lines):
    for k, v in cont.get('dependencies', {}).items():
        _check_blacklist(k, v, result, file, file_lines)
    for k, v in cont.get('devDependencies', {}).items():
        _check_blacklist(k, v, result, file, file_lines)


@load_file
def handle_package_lock_json(cont, result, file, file_lines):
    # Support both old (v1) and new (v2/v3) package-lock.json formats
    # v1 format has top-level 'dependencies'
    # v2/v3 format has 'packages' with keys like 'node_modules/package-name'

    # Try v1 format first
    if 'dependencies' in cont:
        for k, v in cont.get('dependencies', {}).items():
            _check_blacklist(k, v['version'], result, file, file_lines)

    # Try v2/v3 format (packages field)
    if 'packages' in cont:
        for k, v in cont.get('packages', {}).items():
            # Skip the root package (empty key or '')
            if not k or k == '':
                continue
            # Extract package name from 'node_modules/package-name' format
            if k.startswith('node_modules/'):
                package_name = k.replace('node_modules/', '')
                # Handle scoped packages like '@scope/package'
                if package_name.startswith('@'):
                    parts = package_name.split('/')
                    if len(parts) >= 2:
                        package_name = '/'.join(parts[:2])
                else:
                    # Regular packages might have nested paths
                    package_name = package_name.split('/')[0]

                if 'version' in v:
                    _check_blacklist(package_name, v['version'], result, file, file_lines)


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('root',
                        metavar='DIRECTORY',
                        help='root directory of source tree to scan (default: .).',
                        default='.')
    parser.add_argument('--output', metavar='OUTPUT',
                        help='report file name.',
                        type=argparse.FileType('w'),
                        default='-')
    parser.add_argument('--march',
                        help='target processor architecture (default: armv8-a).',
                        default='armv8-a')
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

    args = parser.parse_args()
    if args.march not in SUPPORTED_MARCH:
        parser.exit(1, f'unknown/unsupported arch: {args.march}')

    # Check if a git repo is specified
    if args.git_repo:
        # Import here to avoid circular dependency
        from common.main import clone_git_repo
        # Clone it with given repo, branch or commit
        try:
            clone_git_repo(args.git_repo, args.branch, args.commit, args.root)
        except Exception as e:
            print(f"Error occurred while cloning [{args.git_repo}] : {e}")
            sys.exit(1)

    results = {
        "arch": args.march,
        "errors": [],
        "file_summary": {
            "npm": {
                "count": 0,
                "fileName": "npm Dependencies",
                "loc": 0
            }
        },

        "git_repo": None,
        "issue_summary": {
            "ArchSpecificLibraryIssue": {
                "count": 0,
            }
        },

        "issue_type_config": None,
        "issues": [],

        "language_type": "nodejs",
        "output": None,
        "root_directory": args.root,
        "source_dirs": [],
        "source_files": [],
        "total_issue_count": 0
    }

    root = Path(args.root)
    # Scan all directories for package files, not just the first one
    for folder in root.glob('**/'):
        if (folder / 'package-lock.json').exists():
            handle_package_lock_json(folder / 'package-lock.json', results)
        elif (folder / 'package.json').exists():
            handle_package_json(folder / 'package.json', results)

    # Store git repo info if provided
    if args.git_repo:
        results['git_repo'] = args.git_repo

    json.dump(results, args.output)
