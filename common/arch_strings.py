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

# NOTE: this file contains instruction set architecture related info only!
# NOTE: arch names which contain other arch names comes first!

ARMV8_0 = 'armv8-a'
ARMV8_6_SVE2 = 'armv8.6-a+sve2'
SUPPORTED_MARCH = [ARMV8_0, ARMV8_6_SVE2]
DEFAULT_ARCH = SUPPORTED_MARCH[0]

AARCH64_ARCHS = ['aarch64','arm64', 'arm', 'neon', 'sve2', 'sve', 'aes', 'sha',
                 'tme', 'thumb-2', 'thumb', 'vfpv4-d16', 'vfpv4', 'jazelle']

X86_ARCHS = ['amd64', 'avx', 'avx2', 'avx512', 'i386', 'i586', 'i686', 'ia32',
             'ia64', 'intel', 'intel64', 'm68k', 'sse5', 'sse4.2', 'sse4.1', 'sse4',
             'sse3', 'sse2', 'sse', 'x86_64', 'x86-64', 'x86', 'x64']

OTHER_ARCHS = ['alpha', 'altivec', 'hppa', 'ix86', 'microblaze', 'mips',
               'nios2', 'otherarch', 'power', 'powerpc', 'powerpc32', 'powerpc64',
               'ppc64le', 'ppc64', 'ppc', 's390', 'sh', 'sparc', 'tile']

ALL_ARCHS = AARCH64_ARCHS + X86_ARCHS + OTHER_ARCHS

NON_AARCH64_ARCHS = [x for x in ALL_ARCHS if x not in AARCH64_ARCHS]

NON_X86_ARCHS = [x for x in ALL_ARCHS if x not in X86_ARCHS]

SUPPORTED_COMPILERS = ['clang', 'gcc', 'llvm', 'gnuc', '_msc_ver']

ALL_COMPILERS = ['clang', 'cray', 'flang', 'gcc', 'gfortran', 'gnuc', 'gnug',
                 'ibmcpp', 'ibmxl', 'icc', 'ifort', 'intel_compiler', 'llvm',
                 '_msc_ver', 'pathscale', 'pgi', 'pgic', 'sunpro', 'xlc', 'xlf']
UNSUPPORTED_COMPILERS = [
    'cray', 'flang', 'gfortran', 'gnug',
    'ibmcpp', 'ibmxl', 'icc', 'ifort', 'intel_compiler',
    'pathscale', 'pgi', 'pgic', 'sunpro', 'xlc', 'xlf'
]

AARCH64_UNSUPPORTED_COMPILERS =  [
    'cray', 'flang', 'gfortran', 'gnuc', 'gnug',
    'ibmcpp', 'ibmxl', 'icc', 'ifort', 'intel_compiler', 'llvm',
    '_msc_ver', 'pathscale', 'pgi', 'pgic', 'sunpro', 'xlc', 'xlf'
]

AARCH64_OTHER_UNSUPPORTED_MACROS = ['_WIN32', '_WIN64', '__APPLE__', '__ANDROID__',
                                   '_M_IX86', '_M_X64', '_M_ARM', '_M_THUMB', '_M_ARM64']

SUPPORTED_COMPILERS_ARM = ['gcc', 'clang']

DEFAULT_COMPILER = SUPPORTED_COMPILERS_ARM[0]

SUPPORTED_OS = 'linux'
