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
- libmagic - Required on mac0S (not included by default)

### 2) Enable Python environment

Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell)
```shell
python -m venv .venv
Set-ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### 3) Install requirements

Linux/macOS
```bash
pip3 install -r requirements.txt
```

Windows (PowerShell)
```shell
pip install -r requirements.txt
```

### 4) Set up environment

Linux/macOS
```bash
export PYTHONPATH=/path/to/migrate-ease
```

Windows (PowerShell)
```shell
$env:PYTHONPATH = "\path\to\migrate-ease"
```

### 5) Scan from a code directory

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

---

## `--vendor` and `--instance-type` options

You can optionally derive the target ISA (`--march`) from a **cloud vendor** and **instance type**, instead of specifying `--march` manually.

- `--vendor`: Cloud vendor (e.g., `AWS`, `GCP`, `AliCloud`).
- `--instance-type`: Instance type under the selected vendor (e.g., `c7g`, `c4a`, `c8y`). Requires `--vendor`.
- When `-vendor` and `--instance-type` are provided, the tool derives the target ISA and uses it as `--march` (falling back to the default architecture `-armv8-a` if the derived ISA is not supported).

Usage:

```bash
python3 -m {scanner_name} --vendor <VENDOR> --instance-type <INSTANCE> {scan_path}
```

See the full guide: [vendor-instance-type-usage.md](docs/vendor-instance-type-usage.md)

---

## Built-in help

```bash
python3 -m {scanner_name} -h
```

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

## Web UI

The tool provides a Web UI that makes it easier to run migration compatibility scans and review results in a browser. You can scan a Git repository or upload a source archive, watch live progress logs, and then view/download the final report.

### How to start
```bash
python3 web/server.py {--port <PORT>}
```
- Default port is `8080` if `--port` is not provided.

In your browser, visit:
```
http://<server-host>:8080
```

If you are using the Web UI, a step-by-step guided overlay is available on first visit to help you complete your first scan (Git repository or source archive), configure options (**CSP & Instance**, **Report format**, **Scanner**), and locate the result/download links.

For detailed explanations of each option (CSP/Report Format/Scanner) and what happens during scanning, follow the [Web UI Quick Start Guide](docs/webui-quick-start.md)

---

## Documentation

- [How to read JSON output](docs/json-output.md)
- [Using `--vendor` and `--instance-type` options](docs/vendor-instance-type-usage.md)
- [Web UI quick start guide](docs/webui-quick-start.md)

---
