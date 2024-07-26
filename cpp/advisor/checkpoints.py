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
AARCH64_INTRINSICS = content["COMMON_INTRINSICS"] + content["AARCH64_INTRINSICS"]

AARCH64_INCOMPATIBLE_INTRINSICS = init_checkpoints(
    content['X86_INTRINSICS'] +
    content['OTHER_ARCH_INTRINSICS'] +
    content['INCOMPATIBLE_UCRT_INTRINSICS'], AARCH64_INTRINSICS)

N2_GCC_INTRINSICS = content["COMMON_INTRINSICS"] + content["N2_GCC_INTRINSICS"]

N2_GCC_INCOMPATIBLE_INTRINSICS = init_checkpoints(
    content['X86_INTRINSICS'] +
    content['OTHER_ARCH_INTRINSICS'] +
    content['INCOMPATIBLE_UCRT_INTRINSICS'] +
    content["AARCH64_INTRINSICS"], N2_GCC_INTRINSICS)

N2_CLANG_INTRINSICS = content["COMMON_INTRINSICS"]

N2_CLANG_INCOMPATIBLE_INTRINSICS = init_checkpoints(
    content['X86_INTRINSICS'] +
    content['OTHER_ARCH_INTRINSICS'] +
    content['INCOMPATIBLE_UCRT_INTRINSICS'] +
    content["N2_GCC_INTRINSICS"] +
    content["AARCH64_INTRINSICS"], N2_CLANG_INTRINSICS)

AARCH64_COMPILER_OPTION_CHECKPOINTS = init_checkpoints(
    content["AARCH64_COMPILER_OPTION_CHECKPOINTS"])

AARCH64_INLINE_ASSEMBLY_CHECKPOINTS = init_checkpoints(
    content["AARCH64_INLINE_ASSEMBLY_CHECKPOINTS"])

#  x86/64
X86_INTRINSICS = content['COMMON_INTRINSICS'] + content['X86_INTRINSICS']

X86_INCOMPATIBLE_INTRINSICS = init_checkpoints(
    content['AARCH64_INTRINSICS'] +
    content['OTHER_ARCH_INTRINSICS'], X86_INTRINSICS)

X86_PRAGMA = init_checkpoints(content['X86_PRAGMA'])

#  CPP std lib suggestions
CPP_STD_CODES = init_checkpoints(content['CPP_STD_CODES'])

#  CPP header file suggestions
INCOMPATIBLE_HEADER_FILE = init_checkpoints(content['INCOMPATIBLE_HEADER_FILE'])

# please remember to remove lines for profiling after optimizing :)
end_time = time.time()
print('Initialization of checkpoints took %f seconds.' % (end_time - start_time))
