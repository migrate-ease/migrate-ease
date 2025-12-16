import argparse
import json
import os
import re
import subprocess
import sys

def parse_defines(output):
    macros = {}
    define_pattern = re.compile(r'#define\s+(\S+)(?:\s+(.*))?')

    for line in output.splitlines():
        line = line.strip()
        match = define_pattern.match(line)
        if match:
            key = match.group(1)
            value = match.group(2) if match.group(2) is not None else ""
            macros[key] = value
    return macros

def get_macros(compiler_cmd, isa):
    # Prepare the command
    # We use subprocess to pipe empty input to the compiler
    # cmd structure: compiler [args] -march=isa -dM -E -
    cmd = compiler_cmd.split() + [f'-march={isa}', '-dM', '-E', '-']

    try:
        result = subprocess.run(
            cmd,
            input="",
            capture_output=True,
            text=True,
            check=True
        )
        return parse_defines(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {' '.join(cmd)}: {e.stderr}")
        return None
    except FileNotFoundError:
        print(f"Compiler not found: {cmd[0]}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Generate compiler macros JSON for a given ISA.")
    parser.add_argument("isa", help="The Instruction Set Architecture (e.g., armv9.0-a)")
    parser.add_argument("--gcc-cmd", default="gcc",
                        help="Command to invoke GCC cross-compiler (e.g., aarch64-linux-gnu-gcc)")
    parser.add_argument("--clang-cmd", default="clang",
                        help="Command to invoke Clang cross-compiler (e.g., clang --target=aarch64-linux-gnu)")

    args = parser.parse_args()

    isa = args.isa
    gcc_cmd = args.gcc_cmd
    clang_cmd = args.clang_cmd

    print(f"Generating macros for {isa} using '{gcc_cmd}' and '{clang_cmd}'...")

    gcc_macros = get_macros(gcc_cmd, isa)
    clang_macros = get_macros(clang_cmd, isa)

    if gcc_macros is None:
        print(f"Failed to generate macros for gcc.")

    if clang_macros is None:
        print(f"Failed to generate macros for clang.")

    if gcc_macros is None or clang_macros is None:
        print("Aborting generation due to errors.")
        sys.exit(1)

    data = {
        "gcc": gcc_macros,
        "clang": clang_macros
    }

    output_file = f"macros_{isa}.json"

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Successfully generated {output_file}")

if __name__ == "__main__":
    main()
