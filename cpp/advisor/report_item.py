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

from common.issue import BaseReportItem
from common.report import Report


class ReportItem(BaseReportItem):
    PREPROCESSOR_ERROR = {'type': 'PreprocessorErrorIssue',
                          'des': '检测到目标平台, 该文件可能会进入 #Error 的预处理逻辑.'}
    PRAGMA = {'type': 'PragmaIssue', 'des': '检测到该 #Pragma 可能和目标平台的编译器不兼容.'}
    CPP_LIB_VERSION = {'type': 'CppLibVersionIssue', 'des': '检测到该库版本可能和目标平台的编译器不兼容.'}
    CPP_LIB_RECOMMEND = {'type': 'CppLibRecommendIssue', 'des': '检测到该库可能存在更佳的优化版本.'}
    COMPILER_SPECIFIC = {'type': 'CompilerSpecificIssue',
                         'des': '检测到部分代码和编译器版本或类型强相关, 可能存在兼容性问题.'}
    CPP_STD_CODES = {'type': 'CPPStdCodes', 'des': '检测到与处理器平台内存序相关的 C++ 代码兼容性问题或者可优化逻辑.'}
    INCOMPATIBLE_HEADER_FILE = {'type': 'IncompatibleHeaderFileIssue', 'des': '检测到不兼容的头文件.'}
    INLINE_ASM = {'type': 'InlineAsmIssue', 'des': '检测到在目标平台中使用内联汇编, 可能存在平台兼容性问题.'}
    INTRINSIC = {'type': 'IntrinsicIssue', 'des': '检测到使用了和目标平台存在兼容性问题的 Intrinsic 函数.'}
    ARCH_SPECIFIC_LIBRARY = {'type': 'ArchSpecificLibraryIssue',
                             'des': '检测到在代码中使用了与处理器架构强相关的库, 可能存在兼容性问题.'}
    OLD_CRT = {'type': 'OldCrtIssue', 'des': '检测到使用版本较久远的 C runtime 库, 存在兼容性问题或存在优化的空间.'}
    DEFINE_OTHER_ARCH = {'type': 'DefineOtherArchIssue',
                         'des': '代码中存在其他处理器平台类型的检测逻辑, 可能存在平台兼容性问题.'}
    CROSS_COMPILE = {'type': 'CrossCompileIssue', 'des': '检测到交叉编译兼容性问题.'}
    ASM_SOURCE = {'type': 'AsmSourceIssue',
                  'des': '检测到在汇编源文件中可能存在处理器架构相关的汇编代码, 需要人工进行检查.'}
    CONFIG_GUESS = {'type': 'ConfigGuessIssue',
                    'des': '检测到该 config.guess 文件中不存在和目标平台架构相关的配置, 可能需要适配.'}
    NO_EQUIVALENT_INTRINSIC = {'type': 'NoEquivalentIntrinsicIssue',
                               'des': '检测到使用了在目标平台不存在的 Intrinsic 函数.'}
    NO_EQUIVALENT_INLINE_ASM = {'type': 'NoEquivalentInlineAsmIssue',
                                'des': '检测到使用了在目标平台不存在的内联汇编代码.'}
    NO_EQUIVALENT = {'type': 'NoEquivalentIssue', 'des': 'NO_EQUIVALENT'}
    HOST_CPU_DETECTION = {'type': 'HostCpuDetectionIssue',
                          'des': 'Makefile 中存在处理器平台类型的检测逻辑, 可能存在平台兼容性问题.'}
    BUILD_COMMAND = {'type': 'BuildCommandIssue', 'des': '检测到可能存在的编译构建命令相关的兼容性问题.'}
    AVX256_INTRINSIC = {'type': 'Avx256IntrinsicIssue',
                        'des': '检测到在目标平台使用 AVX256 指令集, 可能存在兼容性问题.'}
    AVX512_INTRINSIC = {'type': 'Avx512IntrinsicIssue',
                        'des': '检测到在目标平台使用 AVX512 指令集, 可能存在兼容性问题.'}
    NO_ISSUES_FOUND_REMARK = {'type': 'NoIssuesFoundRemark', 'des': 'NO_ISSUES_FOUND_REMARK'}
    PORTED_SOURCE_FILES_REMARK = {'type': 'PortedSourceFilesRemark',
                                  'des': '检测到该源文件在目标平台已经有了移植后的版本, 推荐使用目标平台特有的版本.'}
    PORTED_INLINE_ASM_REMARK = {'type': 'PortedInlineAsmRemark',
                                'des': '检测到所使用的 intrinsics 在目标平台已经有了移植后的版本, 推荐使用目标平台特有的版本.'}
    SIGNED_CHAR = {'type': 'SignedCharIssue', 'des': '检测到带符号 Char 型数据兼容性问题.'}

    TYPES = BaseReportItem.TYPES + [
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
        SIGNED_CHAR, ]


Report.REPORT_ITEM = ReportItem
