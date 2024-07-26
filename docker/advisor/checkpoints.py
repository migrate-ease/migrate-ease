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

import os
import time

from ruamel.yaml import YAML

from common.checkpoint import init_checkpoints

start_time = time.time()

current_path = os.path.abspath(os.path.dirname(__file__))
check_points_yml = os.path.abspath(current_path + './../db/check_points.yaml')

if not os.path.isfile(check_points_yml):
    raise RuntimeError('%s not found!' % check_points_yml)

with open(check_points_yml, 'r') as f:
    cnt = f.read()
    yaml = YAML(typ='rt')
    content = yaml.load(cnt)

end_time = time.time()
print('Loading of check_points.yaml took %f seconds.' % (end_time - start_time))

start_time = time.time()

#  aarch64
AARCH64_EXTENSION_PACKAGES = content["AARCH64_PYTHON_EXTENSION_PACKAGES"] \
                             + content["COMMON_AARCH64_AND_X86_PYTHON_EXTENSION_PACKAGES"]

AARCH64_INCOMPATIBLE_EXTENSION_PACKAGES = init_checkpoints(
    content['X86_PYTHON_EXTENSION_PACKAGES'],
    AARCH64_EXTENSION_PACKAGES
)

#  x86/64
X86_EXTENSION_PACKAGES = content['X86_PYTHON_EXTENSION_PACKAGES'] + \
                         content['COMMON_AARCH64_AND_X86_PYTHON_EXTENSION_PACKAGES']

X86_INCOMPATIBLE_EXTENSION_PACKAGES = init_checkpoints(
    content['AARCH64_PYTHON_EXTENSION_PACKAGES']
)

# please remember to remove lines for profiling after optimizing :)
end_time = time.time()
print('Initialization of checkpoints took %f seconds.' % (end_time - start_time))
