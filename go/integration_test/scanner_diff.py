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

import argparse
import json
import os
#  argv1: directory
#  argv2: result.json
import re

checkpoint1 = 'filename'
checkpoint2 = 'issue_type'

tag_error = 0
issue_config_guess = ''

parser = argparse.ArgumentParser()

parser.description = 'please enter the Issue_type:'

parser.add_argument("--src-dir",
                    metavar="src_dir",
                    help='the relative or absolute path of the src dir to be scanned.',
                    default=None)

parser.add_argument("--json-report",
                    metavar="json_report",
                    help='the relative or absolute path of the report in json format.',
                    default=None)

parser.add_argument("--test-dir",
                    metavar="test_armv8-a",
                    help='the record of test dir.',
                    default=None)

args = parser.parse_args()

with open(args.json_report) as f2:
    report = json.load(f2)
    nof_issues = len(report['issues'])

for i in range(nof_issues):
    report['issues'][i]['tig_of_first_traversal'] = 'false'

lib_aarch = ['cygrpc_arm.so', 'libhello_arm.so', 'libnumber_aarch.a', 'libotsclient_aarch.a', '_speedups.so']
issue_lib_aarch = ['_speedups.so']
asm_test_folder="asm_test"
asm_files = ['a_arm64.s', 'b_amd64.s', 'b_amd64.s']
issue_asm_files = ['b_amd64.s']

for filename in os.listdir(args.src_dir):
    if filename == asm_test_folder:
        for asm_filename in os.listdir(os.path.join(args.src_dir, asm_test_folder)):
            if asm_filename in asm_files:
                issue = ''
                if asm_filename in issue_asm_files:
                    issue = 'AsmIssue'

                if issue:
                    file_detect = False

                    for i in range(nof_issues):
                        if report['issues'][i]['filename'] == args.src_dir + asm_test_folder + '/' + asm_filename and report['issues'][i]["issue_type"]['type'] == issue:
                            file_detect = True
                            report['issues'][i]['tig_of_first_traversal'] = 'true'

                    if file_detect == False:
                        print("\033[1;31;40mError: issue %s from file %s is expected but was not detected\033[0m" % (issue, os.path.join(args.src_dir, asm_test_folder, asm_filename)))

    elif os.path.splitext(filename)[1] != ".json":
        if filename in lib_aarch:
            issue = ''
            if filename in issue_lib_aarch:
                    issue = 'GolangLinkLibraryIssue'

            if issue:
                file_detect = False

                for i in range(nof_issues):
                    if report['issues'][i]['filename'] == args.src_dir + filename and report['issues'][i]["issue_type"]['type'] == issue:
                        file_detect = True
                        report['issues'][i]['tig_of_first_traversal'] = 'true'

                if file_detect == False:
                    print("\033[1;31;40mError: issue %s from file %s is expected but was not detected\033[0m" % (issue, args.src_dir + filename))

        else:
            with open(os.path.join(args.src_dir, filename)) as f1:
                lno = 0  # the line number of var l in file "cc_filename"

                for l in f1.readlines():

                    lno += 1

                    if "expect:" in l:
                        issue = re.search("expect:.*", l)
                        issue = issue[0].replace('expect:', '')
                        issue = issue.replace(' ', '')

                        num_lno = 0  # Record the number of lno values corresponding to "expect: InlineAsmIssue" in report
                        for i in range(nof_issues):
                            if report['issues'][i]['lineno'] == lno:
                                if report['issues'][i]["filename"] == args.src_dir + filename and report['issues'][i]["issue_type"]['type'] == issue:
                                    num_lno += 1
                                    report['issues'][i]['tig_of_first_traversal'] = "true"

                        if num_lno > 1:
                            tag_error = 1
                            print("\033[1;31;40mError: issue %s from file %s:%s is detected more than once.\033[0m" % (issue, os.path.abspath(os.path.join(args.src_dir, args.src_dir + filename)), lno))

                        elif num_lno == 0:
                            tag_error = 1
                            print("\033[1;31;40mError: issue %s from file %s:%s is expected but not detected.\033[0m" % (issue, os.path.abspath(os.path.join(args.src_dir, args.src_dir + filename)), lno))

for i in range(nof_issues):
    if report['issues'][i]['tig_of_first_traversal'] != 'true':
        tag_error = 1
        print("\033[1;31;40mError: issue from file %s:%s is detected but was not expected.\033[0m" % (os.path.abspath(os.path.join(args.src_dir, report['issues'][i]["filename"])), report['issues'][i]['lineno']))

if tag_error == 0:
    print("\033[1;32;40mpass\033[0m")
