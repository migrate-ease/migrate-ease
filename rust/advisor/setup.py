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
from distutils.core import setup

from Cython.Build import cythonize
from Cython.Distutils import build_ext

cur_dir = os.path.abspath(os.path.dirname(__file__))
setup_file = os.path.split(__file__)[1]

ext_modules = []

# get all build files
for path, dirs, files in os.walk(cur_dir, topdown=True):
    for file_name in files:
        file = os.path.join(path, file_name)
        if os.path.splitext(file)[1] == '.py':
            if file_name != setup_file:
                ext_modules.append(file)

setup(
    ext_modules=cythonize(
        ext_modules,
        compiler_directives=dict(
            always_allow_keywords=True,
            c_string_encoding='utf-8',
            language_level=3
        )
    ),
    cmdclass=dict(
        build_ext=build_ext
    ),
    script_args=["build_ext", "-b", './build', "-t", './tmp']
)
