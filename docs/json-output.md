# How to read JSON output

Below is an example JSON output:
```json
{
  "branch": null,
  "commit": null,
  "errors": [],
  "file_summary": {},
  "git_repo": null,
  "issue_summary": {},
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
      "snippet": "namespace google { ... }"
    }
  ],
  "language_type": "cpp",
  "march": "armv8-a",
  "output": null,
  "progress": true,
  "quiet": false,
  "remarks": [],
  "root_directory": "/home/my_repo",
  "source_dirs": [],
  "source_files": [],
  "target_os": "OpenAnolis",
  "total_issue_count": 14X
}
```

## Understanding key fields

- `issue_summary`: Statistical summary of the types of issues that the current scanner supports checking.
- `issues`: Specific descriptions of detected issues, including which files and code segments may have potential issues.
  - `checkpoint`: Pattern to identify potential incompatibilities
  - `description`: Description of detected issue
  - `filename`: File in which the issue was detected
  - `issue_type`: Issue type and detailed description
  - `lineno`: Line number of the problematic code
  - `snippet`: Code snippet around the problematic code

## Scanner issue types

For `cpp` scanner, the available issue types are:

- `ArchSpecificLibrary`, `AsmSource`, `Avx256Intrinsic`, `Avx512Intrinsic`,
  `BuildCommand`, `CompilerSpecific`, `ConfigGuess`, `CrossCompile`,
  `DefineOtherArch`, `HostCpuDetection`, `InlineAsm`, `Intrinsic`,
  `NoEquivalent`, `NoEquivalentInlineAsm`, `NoEquivalentIntrinsic`, `OldCrt`,
  `PragmaSimd`, `PreprocessorError`

To get issue types of other scanners, use the built-in help:

```bash
python3 -m {scanner_name} -h
```
