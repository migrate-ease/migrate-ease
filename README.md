# MigrateEase

MigrateEase is an innovative project designed to analyze codebases specifically for x86_64 architectures and offers tailored suggestions aimed at facilitating the migration process to aarch64. This tool streamlines the transition, ensuring a smooth and efficient evolution of your software to leverage the benefits of aarch64 architecture.

## Install
```
# Enable Python Environment Linux/Mac:
python3 -m venv .venv
source .venv/bin/activate
# install dependencies
pip3 install -r requirement.txt
```

## Usage
```
python3 -m {scanner_name} --output {result_file_name}.json --arch {arch} {scan_path}'
```

Parameters
{scanner_name}: The name of the scanner, which can be one of cpp, docker, js, python, rust.
{result_file_name}: The name of the output result file (without the extension).
{arch}: The architecture type, x86_64 or aarch64.
{scan_path}: The path to the code that needs to be scanned.
