#  argv1: directory
#  argv2: result.json
import argparse
import json
import os
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

args = parser.parse_args()

with open(args.json_report) as f2:
    report = json.load(f2)
    nof_issues = len(report['issues'])

for i in range(nof_issues):
    report['issues'][i]['tig_of_first_traversal'] = 'false'

for filename in os.listdir(args.src_dir):

    if os.path.splitext(filename)[1] != ".json":

        with open(os.path.join(args.src_dir, filename)) as f1:

            lno = 0  # the line number of var l in file "cc_filename"

            for l in f1.readlines():

                lno += 1

                if "expect:" in l:
                    issue = re.search("expect:.*", l)
                    issue = issue[0].replace('expect:', '')
                    issue = issue.replace(' ', '')

                    if filename == "config.guess":
                        if issue == "ConfigGuessIssue":
                            issue_config_guess = issue
                            continue

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
        if report['issues'][i]["issue_type"]['type'] == 'ConfigGuessIssue':
            if issue_config_guess != 'ConfigGuessIssue':
                tag_error = 1
                print("\033[1;31;40mError: issue from file %s:%s is detected but was not expected.\033[0m" % (os.path.abspath(os.path.join(args.src_dir, report['issues'][i]["filename"])), report['issues'][i]['lineno']))
        else:
            tag_error = 1
            print("\033[1;31;40mError: issue from file %s:%s is detected but was not expected.\033[0m" % (os.path.abspath(os.path.join(args.src_dir, report['issues'][i]["filename"])), report['issues'][i]['lineno']))

if tag_error == 0:
    print("\033[1;32;40mpass\033[0m")
