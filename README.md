MigrateEase
============

Migrate-ease is maintained by the OpenAnolis Arm Working Group. This is a fork of [Porting advisor](https://github.com/arm-hpc/porting-advisor), an open source project by the ARM High Performance Computing group.

It is an innovative project designed to analyze codebases specifically for x86_64 architectures and offers tailored suggestions aimed at facilitating the migration process to aarch64. This tool streamlines the transition, ensuring a smooth and efficient evolution of your software to leverage the benefits of aarch64 architecture. At present, this tool only supports codebase migration to Linux. It can be run on Arm or non-Arm based machines. The tool does not modify any code, it does not provide API level recommendations, and it does not send any data back to OpenAnolis.

**PLEASE NOTE: Even though we do our best to identify known incompatibilities, we still recommend performing appropriate tests on your application before going to Production.**

This tool scans all files in a source tree, regardless of whether they are included by the build system or not. Currently, the tool supports the following languages/dependencies:

* C, C++
    * Inline assembly with no corresponding aarch64 inline assembly
    * Assembly code with no corresponding aarch64 assembly code
    * Use of architecture specific intrinsic
    * Use of architecture specific compilation options
    * Preprocessor errors that trigger when compiling on aarch64
    * Compiler specific code guarded by compiler specific pre-defined macros
    * Missing aarch64 architecture detection in Makefile, Config.guess scripts
    * Linking against libraries that are not available on the aarch64 architecture

* Go
    * Inline assembly with no corresponding aarch64 inline assembly
    * Assembly code with no corresponding aarch64 assembly code
    * Use of architecture specific intrinsic
    * Linking against libraries that are not available on the aarch64 architecture

* Python
    * Inline assembly with no corresponding aarch64 inline assembly
    * Use of architecture specific intrinsic
    * Linking against libraries that are not available on the aarch64 architecture
    * Use of architecture specific packages

* Rust
    * Inline assembly with no corresponding aarch64 inline assembly
    * Use of architecture specific intrinsic
    * Linking against libraries that are not available on the aarch64 architecture

* Java
    * Use of architecture specific JAR packages
    * Dependency versions in pom.xml file
    * A feature to detect native calls in Java source code
    * Compatible version recommendation

* Dockerfile
    * Use of architecture specific plugin
    * The base image that dockfile is based on does not support aarch64

# How to run:

**Pre-requisites**
- Python 3.6.8 or above (with PIP3 module installed).
- unzip

**Enable Python Environment**

Linux/Mac:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Install requirements**

```bash
pip3 install -r requirements.txt
```

**Setup environment**
```bash
export PYTHONPATH=/path/to/migrate-ease
```

**Run tool (console output)**

```bash
python3 -m {scanner_name} --arch {arch} {scan_path}
```

**Run tool (JSON report)**

```bash
python3 -m {scanner_name} --output {result_file_name}.json --arch {arch} {scan_path}
```

Parameters:
- `{scanner_name}`: The name of the scanner, which can be one of `cpp`, `docker`, `go`, `js`, `java`, `python`, `rust`.
- `{result_file_name}`: The name of the output result file (without the extension).
- `{arch}`: The target instruction set architecture (default: aarch64).
- `{scan_path}`: The path to the code directory that needs to be scanned.

You can also specify the code to be scanned through the Git repository address.
```bash
python3 -m {scanner_name} --output {result_file_name}.json --arch {arch} --git-repo {repo} {scan_path}
```
**NOTE: `{scan_path}` is a directory that user would like to this tool to create and clone to.**

For more information on how to modify issues reported, use the tool's built-in help:

```
python3 -m {scanner_name} -h
```

# Integration test

This tool also includes comprehensive integration tests. Integration tests ensure that various modules work correctly together after integration, identify interface issues, verify functionality, detect defects, improve system stability, and ensure compatibility. Through integration tests, this tool can provide higher quality and reliability, meeting various user needs.

**NOTE: Need to set the PYTHONPATH to the root directory of the migrate-ease.**

```bash
export PYTHONPATH=/path/to/migrate-ease
cd <scanner_name>/integration_test
./test
```

# Example to generate JSON report
```
$ python3 -m cpp --git-repo https://github.com/protocolbuffers/protobuf.git --branch v2.5.0 --output result.json --arch aarch64 /home/my_repo
```
After the above has been executed successfully, you will see a JSON format file at current directory as `result.json`.

# How to read JSON output
```json
{
    "arch": "aarch64",
    "branch": null,
    "commit": null,
    "errors": [],
    "file_summary": {
    },
    "git_repo": null,
    "issue_summary": {
    },
    "issue_type_config": null,
    "issues": [
        {
            "checkpoint": null,
            "description": "preprocessor error: #error \"We require at least vs2005 for MemoryBarrier\"",
            "filename": "/home/my_repo/src/google/protobuf/stubs/atomicops_internals_x86_msvc.h",
            "issue_type": {
                "des": "Target platform may enter the #error preprocessing logic.",
                "type": "PreprocessorErrorIssue"
            },
            "lineno": 46,
            "snippet": "namespace google {\nnamespace protobuf {\nnamespace internal {\n\ninline Atomic32 NoBarrier_AtomicIncrement(volatile Atomic32* ptr,\n                                          Atomic32 increment) {\n  return Barrier_AtomicIncrement(ptr, increment);\n}\n\n#if !(defined(_MSC_VER) && _MSC_VER >= 1400)\n<font style='color:red;'>#error \"We require at least vs2005 for MemoryBarrier\"</font>\n#endif\n\ninline Atomic32 Acquire_CompareAndSwap(volatile Atomic32* ptr,\n                                       Atomic32 old_value,\n                                       Atomic32 new_value) {\n  return NoBarrier_CompareAndSwap(ptr, old_value, new_value);\n}\n\ninline Atomic32 Release_CompareAndSwap(volatile Atomic32* ptr,\n                                       Atomic32 old_value,\n"
        },
    ],
    "language_type": "cpp",
    "march": null,
    "output": null,
    "progress": true,
    "quiet": false,
    "remarks": [],
    "root_directory": "/home/my_repo",
    "source_dirs": [
    ],
    "source_files": [
    ],
    "target_os": "OpenAnolis",
    "total_issue_count": 14
}
```

The `issue_summary` is a statistical summary of the types of issues that the current scanner supports checking. For `cpp` scanner, the available issue types are:

- ArchSpecificLibrary, AsmSource, Avx256Intrinsic, Avx512Intrinsic,
  BuildCommand, CompilerSpecific, ConfigGuess, CrossCompile,
  DefineOtherArch, HostCpuDetection, InlineAsm, Intrinsic,
  NoEquivalent, NoEquivalentInlineAsm, NoEquivalentIntrinsic, OldCrt,
  PragmaSimd, PreprocessorError

To get issue types of other language scanner, use the tool's built-in help:

```
python3 -m {scanner_name} -h
```

The `issues` provide specific descriptions of the detected issues, including which files and specific code segments may have potential issues.
- `checkpoint`: A pattern to identify potential incompatibilities.
- `description`: The descriptions of the detected issues.
- `filename`: The file in which issues were detected.
- `issue_type`: The types of issues, including detailed descriptions of the errors.
- `lineno`: The line number of the problematic code.
- `snippet`: The code segment of the problematic code.
