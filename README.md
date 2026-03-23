# MigrateEase

Migrate-ease is maintained by the OpenAnolis Arm Working Group. This is a fork of [Porting advisor](https://github.com/arm-hpc/porting-advisor), an open source project by the ARM High Performance Computing group.

It is an innovative project designed to analyze codebases specifically for x86_64 architectures and offers tailored suggestions aimed at facilitating the migration process to aarch64. This tool streamlines the transition, ensuring a smooth and efficient evolution of your software to leverage the benefits of aarch64 architecture. At present, this tool only supports codebase migration to Linux. It can be run on Arm or non-Arm based machines. The tool does not modify any code, it does not provide API level recommendations, and it does not send any data back to OpenAnolis.

**Please note:** Even though we do our best to identify known incompatibilities, we still recommend performing appropriate tests on your application before going to production.

---

## What it scans (languages & dependencies)

This tool scans **all files in a source tree**, regardless of whether they are included by the build system or not.

Currently, the tool supports the following languages/dependencies:

### C / C++
- Inline assembly with no corresponding aarch64 inline assembly
- Assembly code with no corresponding aarch64 assembly code
- Use of architecture specific intrinsic
- Use of architecture specific compilation options
- Preprocessor errors that trigger when compiling on aarch64
- Compiler specific code guarded by compiler specific pre-defined macros
- Missing aarch64 architecture detection in Makefile, Config.guess scripts
- Linking against libraries that are not available on the aarch64 architecture

### Go
- Inline assembly with no corresponding aarch64 inline assembly
- Assembly code with no corresponding aarch64 assembly code
- Use of architecture specific intrinsic
- Linking against libraries that are not available on the aarch64 architecture

### Python
- Inline assembly with no corresponding aarch64 inline assembly
- Use of architecture specific intrinsic
- Linking against libraries that are not available on the aarch64 architecture
- Use of architecture specific packages

### Rust
- Inline assembly with no corresponding aarch64 inline assembly
- Use of architecture specific intrinsic
- Linking against libraries that are not available on the aarch64 architecture

### Java
- Use of architecture specific JAR packages
- Dependency versions in pom.xml file
- A feature to detect native calls in Java source code
- Compatible version recommendation

### Dockerfile
- Use of architecture specific plugin
- The base image that dockerfile is based on does not support aarch64

---

## How to run

### 1) Pre-requisites
- Python 3.6.8 or above (with PIP3 module installed)
- unzip

### 2) Enable Python environment

Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install requirements

Linux/macOS
```bash
pip3 install -r requirements.txt
```

### 4) Setup environment

Linux/macOS
```bash
export PYTHONPATH=/path/to/migrate-ease
```

### 5) Run the tool

#### Console output

```bash
python3 -m {scanner_name} --march {arch} {scan_path}
```

#### JSON report output

```bash
python3 -m {scanner_name} --output {result_file_name}.json --march {arch} {scan_path}
```

**Parameters:**
- `{scanner_name}`: Scanner name: `cpp`, `docker`, `go`, `js`, `java`, `python`, `rust`
- `{result_file_name}`: Output result file name (without extension)
- `{arch}`: Target processor architecture.  It follows the same semantics as GCC's `-march`, specifying the target architecutre and feature set. Supported: `armv8-a` (default) and `armv8.6-a+sve2`.
- `{scan_path}`: Path to the code directory to scan

### 6) Scan from a Git repository

```bash
python3 -m {scanner_name} --output {result_file_name}.json --march {arch} --git-repo {repo} {scan_path}
```

**Note:** `{scan_path}` is a directory that user would like this tool to create and clone to.

### Built-in help

```bash
python3 -m {scanner_name} -h
```

> See also: [Using `--csp` and `--instance`](docs/csp-instance-options.md) for instance-based `--march` selection.

---

## Integration test

This tool includes comprehensive integration tests. Integration tests ensure that various modules work correctly together after integration, identify interface issues, verify functionality, and detect regressions.

**Note:** Need to set the `PYTHONPATH` to the root directory of the migrate-ease.

```bash
export PYTHONPATH=/path/to/migrate-ease
cd <scanner_name>/integration_test
./test
```

---

## Example: generate a JSON report

```bash
python3 -m cpp \
  --git-repo https://github.com/protocolbuffers/protobuf.git \
  --branch v2.5.0 \
  --output result.json \
  --march armv8-a \
  /home/my_repo
```

After the above has been executed successfully, you will see a JSON format file at current directory as `result.json`.

---

## Documentation

- [How to read JSON output](docs/json-output.md)
