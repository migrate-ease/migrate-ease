"""
Copyright 2026 Arm Ltd.

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

"""
scan: run multiple language scanners in parallel.

- Runs each language scanner as a subprocess:
    python -m <language> ...
- If --output is provided, it will be split per language:
    report.json -> report.cpp.json, report.go.json, ...
- If --output is not provided, scan will not force generating reports.
"""

import argparse
import subprocess
import sys
import os

from concurrent.futures import ThreadPoolExecutor, as_completed


LANGUAGES = ['cpp', 'docker', 'go', 'java', 'js', 'python', 'rust']

def split_languages(value):
    langs = []
    for item in value.lower().split(','):
        item = item.strip()
        if item:
            langs.append(item)

    if not langs:
        raise argparse.ArgumentTypeError('--language must not be empty')

    return langs

def strip_output_args(args):
    """
    Remove existing --output from arg list.

    Handles:
      --output FILE
      --output=FILE
    """
    out = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == '--output':
            i += 2
            continue
        if a.startswith('--output='):
            i += 1
            continue
        out.append(a)
        i += 1
    return out

def per_language_output(base_output, language):
    """
    Split base output path per language.

    Examples:
      report.json -> report.cpp.json
      aaa         -> aaa.cpp
    """
    root, ext = os.path.splitext(base_output)
    if ext:
        return root + '.' + language + ext
    return base_output + '.' + language

def prefix_lines(text, prefix):
    if not text:
        return []
    lines = text.splitlines()
    return [prefix + line for line in lines]

def run_one(language, rest_args, base_output):
    cmd = [sys.executable, '-m', language]

    output_path = None
    call_args = list(rest_args)

    if base_output:
        output_path = per_language_output(base_output, language)
        call_args = strip_output_args(call_args)
        call_args += ['--output', output_path]

    proc = subprocess.run(cmd + call_args,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          text=True)

    return {
        'language': language,
        'returncode': proc.returncode,
        'stdout': proc.stdout,
        'stderr': proc.stderr,
        'output': output_path,
    }

def main(argv=None):
    parser = argparse.ArgumentParser(
        prog='scan',
        description='Run multiple migrate-ease language scanners in parallel.')

    parser.add_argument('--language',
                        required=True,
                        type=split_languages,
                        help='Comma-separated list of languages to scan. Use "all" to select all supported languages. Supported: {}.'.format(', '.join(LANGUAGES)))

    # Parse --output here only for splitting per language.
    parser.add_argument('--output',
                        default=None,
                        help='Base report file name. If set, output will be split per language.')

    args, rest = parser.parse_known_args(argv)

    if args.language:
        languages = args.language
        if 'all' in languages:
            # If 'all' is included, use the full set
            selected_languages = LANGUAGES
        else:
            # Filter out unsupported languages
            selected_languages = [lang for lang in languages if lang in LANGUAGES]
    else:
        selected_languages = []

    base_output = args.output

    results = []
    failed_languages = []

    with ThreadPoolExecutor(max_workers=len(selected_languages)) as executor:
        future_map = {}
        for lang in selected_languages:
            future = executor.submit(run_one, lang, rest, base_output)
            future_map[future] = lang

        for future in as_completed(future_map):
            results.append(future.result())

    results.sort(key=lambda x: x['language'])

    for r in results:
        lang = r['language']

        # Header line per language
        if r['output']:
            print('[scan:%s] output=%s' % (lang, r['output']))
        else:
            print('[scan:%s]' % lang)

        # Print stdout/stderr line-by-line with prefix
        for line in prefix_lines(r['stdout'], '[scan:%s] ' % lang):
            print(line)
        for line in prefix_lines(r['stderr'], '[scan:%s] ' % lang):
            print(line, file=sys.stderr)

        if r['returncode'] != 0:
            failed_languages.append(lang)

    if failed_languages:
        print('[scan] failed languages: %s' % ','.join(failed_languages),
              file=sys.stderr)
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
