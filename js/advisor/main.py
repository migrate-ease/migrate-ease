import argparse
import functools
import json
import pathlib
from pathlib import Path


def _check_blacklist(package_name, version, result, file, file_lines):
    version = tuple(version.split('.'))
    msg = None
    if package_name == 'serialport':
        if version <= ('7', '1', '5'):
            msg = '请升级 serialport 到 >= 8.0.5 的版本'
    elif package_name == 'node-sass':
        if version <= ('6', '0', '7'):
            msg = '请升级 node-sass 到 >= 6.0.1 的版本'
    elif package_name == 'sass-loader':
        if version <= ('6', '0', '7'):
            msg = 'sass-loader <= 6.0.7 不支持倚天平台'
    elif package_name == 'hiredis':
        msg = 'hiredis 包已被弃用，不支持 ARM 平台'
    elif package_name == 'puppeteer':
        msg = '倚天平台上需要手动安装 chromium'
    elif package_name == 'fsevents':
        msg = 'fsevents 不支持 ARM 平台'
    elif package_name in ('phantomjs', 'phantomjs-prebuilt'):
        msg = f'{package_name} 已被弃用，不支持 ARM 平台'
    elif package_name == 'grpc':
        if version < ('1', '24', '10'):
            msg = 'grpc 包已停止更新，请使用 @grpc/grpc-js'

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
                "des": "检测到不兼容的 NPM 包",
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
    for k, v in cont.get('dependencies', {}).items():
        _check_blacklist(k, v['version'], result, file, file_lines)


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
    parser.add_argument('--arch',
                        help='target instruction set architecture (default: aarch64).',
                        default='aarch64')
    args = parser.parse_args()
    if args.arch != 'aarch64':
        parser.exit(1, f'unknown/unsupported arch: {args.arch}')

    results = {
        "arch": args.arch,
        "errors": [],
        "file_summary": {
            "npm": {
                "count": 0,
                "fileName": "npm 依赖文件",
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
    for folder in root.glob('**/'):
        if (folder / 'package-lock.json').exists():
            handle_package_lock_json(folder / 'package-lock.json', results)
        elif (folder / 'package.json').exists():
            handle_package_json(folder / 'package.json', results)
        else:
            continue
        break

    json.dump(results, args.output)
