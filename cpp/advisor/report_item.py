"""
Copyright 2020-2023 Alibaba Inc.
Copyright 2017-2025 Arm Ltd.

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

from common.localization import _

PREPROCESSOR_ERROR = {'type': 'PreprocessorErrorIssue',
                      'des': _('Target platform may enter the #error preprocessing logic')}
PRAGMA = {'type': 'PragmaIssue', 'des': _("This #Pragma may be incompatible with the target platform's compiler.")}
CPP_LIB_VERSION = {'type': 'CppLibVersionIssue', 'des': _("This library version may be incompatible with the target platform's compiler")}
CPP_LIB_RECOMMEND = {'type': 'CppLibRecommendIssue', 'des': _('A better-optimized version of this library may be available')}
COMPILER_SPECIFIC = {'type': 'CompilerSpecificIssue',
                     'des': _("Code is strongly tied to a compiler version or type, which may lead to compatibility issues")}
CPP_STD_CODES = {'type': 'CPPStdCodes', 'des': _("Compatibility issues or optimization opportunities related to Cpp source and memory order on the target platform")}
INCOMPATIBLE_HEADER_FILE = {'type': 'IncompatibleHeaderFileIssue', 'des': _("Incompatible header files")}
INLINE_ASM = {'type': 'InlineAsmIssue', 'des': _("Use of inline assembly may lead to target platform compatibility issues")}
INTRINSIC = {'type': 'IntrinsicIssue', 'des': _("Use of intrinsics that have compatibility issues with the target platform")}
ARCH_SPECIFIC_LIBRARY = {'type': 'ArchSpecificLibraryIssue',
                         'des': _("Use of libraries strongly tied to the processor architecture, which may lead to compatibility issues.")}
OLD_CRT = {'type': 'OldCrtIssue', 'des': _("Use of an older version of the C runtime library, which may have compatibility issues or present opportunities for optimization")}
DEFINE_OTHER_ARCH = {'type': 'DefineOtherArchIssue',
                     'des': _("Logic in the code that checks for other processor platform types, which may lead to compatibility issues")}
CROSS_COMPILE = {'type': 'CrossCompileIssue', 'des': _("Cross-compilation compatibility issues")}
ASM_SOURCE = {'type': 'AsmSourceIssue',
              'des': _("Potentially architecture-specific assembly code in the source files that requires manual inspection")}
CONFIG_GUESS = {'type': 'ConfigGuessIssue',
                'des': _("Config.guess file does not contain configurations related to the target platform architecture, which may require adaptation")}
NO_EQUIVALENT_INTRINSIC = {'type': 'NoEquivalentIntrinsicIssue',
                           'des': _("Use of intrinsic functions that do not exist on the target platform")}
NO_EQUIVALENT_INLINE_ASM = {'type': 'NoEquivalentInlineAsmIssue',
                            'des': _("Use of inline assembly code that does not exist on the target platform")}
NO_EQUIVALENT = {'type': 'NoEquivalentIssue', 'des': 'NO_EQUIVALENT'}
HOST_CPU_DETECTION = {'type': 'HostCpuDetectionIssue',
                      'des': _("Logic for processor platform types in the Makefile, which may lead to platform compatibility issues")}
BUILD_COMMAND = {'type': 'BuildCommandIssue', 'des': _("Potential compatibility issues related to the compilation build commands")}
AVX256_INTRINSIC = {'type': 'Avx256IntrinsicIssue',
                    'des': _("Use of AVX256 instructions on the target platform lead to compatibility issues")}
AVX512_INTRINSIC = {'type': 'Avx512IntrinsicIssue',
                    'des': _("Use of AVX512 instructions on the target platform lead to compatibility issues")}
NO_ISSUES_FOUND_REMARK = {'type': 'NoIssuesFoundRemark', 'des': 'NO_ISSUES_FOUND_REMARK'}
PORTED_SOURCE_FILES_REMARK = {'type': 'PortedSourceFilesRemark',
                              'des': _("The source file already has a ported version for the target platform. It is recommended to use the platform-specific version")}
PORTED_INLINE_ASM_REMARK = {'type': 'PortedInlineAsmRemark',
                            'des': _("Intrinsics used already have a ported version for the target platform. It is recommended to use the platform-specific version")}
SIGNED_CHAR = {'type': 'SignedCharIssue', 'des': _("Compatibility issues with signed char type data")}

CPP_REPORT_TYPES = [
    PREPROCESSOR_ERROR,
    PRAGMA,
    COMPILER_SPECIFIC,
    CPP_STD_CODES,
    CPP_LIB_VERSION,
    CPP_LIB_RECOMMEND,
    INCOMPATIBLE_HEADER_FILE,
    INLINE_ASM,
    INTRINSIC,
    ARCH_SPECIFIC_LIBRARY,
    OLD_CRT,
    DEFINE_OTHER_ARCH,
    CROSS_COMPILE,
    ASM_SOURCE,
    CONFIG_GUESS,
    NO_EQUIVALENT_INTRINSIC,
    NO_EQUIVALENT_INLINE_ASM,
    NO_EQUIVALENT,
    HOST_CPU_DETECTION,
    BUILD_COMMAND,
    AVX256_INTRINSIC,
    AVX512_INTRINSIC,
    NO_ISSUES_FOUND_REMARK,
    PORTED_SOURCE_FILES_REMARK,
    PORTED_INLINE_ASM_REMARK,
    SIGNED_CHAR,
    ]
