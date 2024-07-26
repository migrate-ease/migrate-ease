# Porting Advisor

This tool scans for potential unported or non-portable code in source code
trees.

The following types of issue are reported by default:
* Inline assembly with no corresponding aarch64 inlne assembly.
* Asssembly source files with no corresponding aarch64 assembly source files.
* Missing aarch64 architecture detection in autoconf config.guess scripts.
* Linking against libraries that are not available on the aarch64 architecture.
* Use of architecture specific intrinsics.
* Preprocessor errors that trigger when compiling on aarch64.
* Use of old Visual C++ runtime (Windows specific).

The following types of issues are detected, but not reported by default:
* Compiler specific code guarded by compiler specific pre-defined macros.

The following types of cross-compile specific issues are detected, but not
reported by default.
* Architecture detection that depends on the host rather than the target.
* Use of build artifacts in the build process.

# Install

To install the dependencies:
```python
python3 -m pip install -r requirements.txt --user
```

# Usage
```
usage: porting-advisor [-h] [--arch ARCH] [--issue-types ISSUE_TYPES]
                       [--no-progress] [--output OUTPUT]
                       [--output-format OUTPUT_FORMAT] [--quiet]
                       [--target-os TARGET_OS] [--target-compiler COMPILER]
                       [--warning-level LEVEL] [--version]
                       DIRECTORY

Produces an aarch64 porting readiness report.

positional arguments:
  DIRECTORY             root directory of source tree (default: .)

optional arguments:
  -h, --help            show this help message and exit
  --arch ARCH           Instruction set schema name (armv8.6-a+sve2, arm64, default: armv8.6-a+sve2)
  --issue-types ISSUE_TYPES
                        modify the types of issue that are reported (default:
                        -CompilerSpecific,-CrossCompile,-NoEquivalent)
  --no-progress         don't show progress bar
  --output OUTPUT       output file name
  --output-format OUTPUT_FORMAT
                        output format:
                        auto,csv_issue_type_count_by_file,csv,json,html,text
                        (default: auto)
  --quiet               suppress file errors
  --target-os TARGET_OS
                        target operating system: all,linux,windows (default:
                        linux)
  --target-compiler COMPILER
                        target operating system: gcc, clang (default:
                        gcc)
  --warning-level LEVEL
                        warning-level: L1, L2 (default:L1)                                        
  --version             show program's version number and exit

ArchType:
  armv8.6-a+sve2, arm64

Use:
  --issue-types=+CompilerSpecific to enable reporting of use of
    compiler-specific macros.
  --issue-types=+CrossCompile to enable reporting of cross-compile
    specific issues.
  --issue-types=+NoEquivalent to enable reporting of aarch64 ported
    code that does not use intrinsics inline assembly versus other
    architectures.

Available issue types:
  ArchSpecificLibrary, AsmSource, Avx256Intrinsic, Avx512Intrinsic,
  BuildCommand, CompilerSpecific, ConfigGuess, CrossCompile,
  DefineOtherArch, HostCpuDetection, InlineAsm, Intrinsic,
  NoEquivalent, NoEquivalentInlineAsm, NoEquivalentIntrinsic, OldCrt,
  PragmaSimd, PreprocessorError

```

# Hints:
- CompilerSpecificIssue is not supported by the scanner now.
- armv8.6-a+sve2 parameter indicates target arch is N2 and target os is with linux.
- warning level and target compiler only works when arch is armv8.6-a+sve2.

And refer to `./run.sh` for more details.

# Caveats

This tool scans all files in a source tree, regardless of whether they are
included by the build system or not. As such it may erroneously report issues in
files that appear in the source tree but are excluded by the build system.

# License

Copyright 2020-2023 Alibaba Ltd.

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
