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

import re


def find_matching_line_num(lines, lineno, pattern):
    """
    Find the actual matching line number
    """

    real_lineno = lineno
    if pattern is None:
        return real_lineno

    while lineno > 0:

        line = lines[lineno]

        match = re.compile(r'%s' % pattern).search(line)
        if match:
            real_lineno = lineno
            break
        lineno = lineno - 1

    return real_lineno
