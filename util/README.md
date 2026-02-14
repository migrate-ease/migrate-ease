# Utility Scripts

This directory contains utility scripts for the `migrate-ease` project.

## `generate_macros_json.py`

This script generates a JSON file containing predefined compiler macros for a specific Instruction Set Architecture (ISA). It captures macros from both GCC and Clang.

### Prerequisites

- GCC and Clang compilers installed (optionally cross-compilers if generating for non-host architectures).
- Python 3.

### Usage

```bash
python3 generate_macros_json.py <ISA> [options]
```

#### Arguments:

- `isa`: The target Instruction Set Architecture (e.g., `armv8-a`, `armv9-a`).

#### Options:

- `--gcc-cmd`: The command to invoke the GCC compiler (default: `gcc`). Useful for cross-compilers (e.g., `aarch64-linux-gnu-gcc`).
- `--clang-cmd`: The command to invoke the Clang compiler (default: `clang`). Useful for cross-compilers (e.g., `clang --target=aarch64-linux-gnu`).

### Output

The script generates a file named `macros_<ISA>.json` in the current directory. The JSON format is:

```json
{
    "gcc": {
        "MACRO_NAME": "value",
        ...
    },
    "clang": {
        "MACRO_NAME": "value",
        ...
    }
}
```

These JSON files are used by the C++ advisor to evaluate predefined macros on target platforms.
