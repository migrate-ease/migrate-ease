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

import re
import os
from ruamel.yaml import YAML


class Checkpoint:
    #  (?aiLmsux)
    #  ---
    #  (One or more letters from the set 'a', 'i', 'L', 'm', 's', 'u', 'x'.)
    #  The
    #  group matches the empty string; the letters set the corresponding flags:
    #  re.A (ASCII-only matching),
    #  re.I (ignore case),
    #  re.L (locale dependent),
    #  re.M (multi-line),
    #  re.S (dot matches all),
    #  re.U (Unicode matching)
    #  re.X (verbose),
    #  for the entire regular expression. (The flags are described in Module
    #  Contents.) This is useful if you wish to include the flags as part of the
    #  regular expression, instead of passing a flag argument to the
    #  re.compile() function. Flags should be used first in the expression
    #  string.
    re_func_name = re.compile(r'(?i)([0-9a-zA-Z_]+)\s*\(')

    def __init__(self, checkpoint):

        if checkpoint is None:
            raise ValueError("checkpoint cannot be None")

        try:
            self.section = checkpoint
            self.isa = checkpoint.get("isa", default='').split(',')
            self.signature = checkpoint.get('signature', default='')
            self.pattern = checkpoint.get('pattern', default='')
            self.notes = checkpoint.get('notes', default='')
            self.help = checkpoint.get('help', default='')
            self.func_name = None

            #  in case there's no pattern provided, we use function name as the
            #  pattern, the function name was extracted from the fuction
            #  signature
            if not self.pattern:

                # extract the function name from the signature
                func_name = self.re_func_name.search(self.signature).group(1)

                # if function name found, compile it
                if func_name:
                    self.func_name = func_name
                    self.pattern_compiled = re.compile(r'(?i)([ ]{})\s*\('.format(func_name))
                else:
                    raise ValueError('invalid checkpoint %s' % checkpoint)

            else:
                self.pattern_compiled = re.compile(format(self.pattern))

        except BaseException:
            raise
def load_checkpoints(file_path):
    if not os.path.isfile(file_path):
        raise RuntimeError('[%s] not found!' % file_path)
    with open(file_path, 'r') as f:
        cnt = f.read()
        yaml = YAML(typ='rt')
        _content = yaml.load(cnt)

    return _content

def init_checkpoints(checkpoints, exclude_checkpoints=None):
    _checkpoints = []
    if exclude_checkpoints is None:
        exclude_checkpoints = []

    exclude_checkpoints_names = [Checkpoint(_).func_name for _ in exclude_checkpoints]

    for _ in checkpoints:
        cp = Checkpoint(_)

        if cp.pattern:
            _checkpoints.append(cp)
            continue

        if cp.func_name not in exclude_checkpoints_names:
            _checkpoints.append(cp)
            continue

    return _checkpoints
