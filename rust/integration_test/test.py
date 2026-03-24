"""
Copyright 2026 Arm Ltd.

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


import os
import sys
import subprocess
from pathlib import Path

# Enable ANSI colors on Windows
try:
    from colorama import init as colorama_init
    colorama_init()
except Exception:
    pass

GREEN = "\033[0;32m"
ENDMARK = "\033[m"

def run(cmd, cwd=None):
    try:
        # Use sys.executable to ensure the same Python on Windows
        res = subprocess.run(cmd, cwd=cwd, check=False)
        return res.returncode
    except Exception as e:
        print(f"Failed to run: {' '.join(map(str, cmd))}\nError: {e}")
        return 1

def main():
    script_dir = Path(__file__).resolve().parent
    main_dir = script_dir.parent

    # Must be run in the directory where this script is located
    os.chdir(script_dir)

    # Use glob without trailing slash for Windows compatibility
    for entry in sorted(script_dir.glob("test_*")):
        if not entry.is_dir():
            print(f"Skipping non-directory: {entry.name}")
            continue

        test_folder = entry.name
        print(f"=============== Running {test_folder} ... ===============")

        arch = test_folder.replace("test_", "", 1)
        if arch == "":
            print(f"{GREEN}{test_folder} is invalid, should be test_<arch_name>, skip.{ENDMARK}")
            continue

        print(f"running sub-test for {arch}")
        out_dir = script_dir / test_folder
        out_json = out_dir / f"{arch}.json"
        cmd = [
            sys.executable, str(main_dir / "__main__.py"),
            "--output-format", "json",
            "--output", str(out_json),
            "--march", arch,
            str(out_dir),
        ]
        rc = run(cmd)
        if rc == 0:
            print("running scanner diff")
            diff_cmd = [
                sys.executable, str(script_dir / "scanner_diff.py"),
                "--src-dir", str(out_dir),
                "--json-report", str(out_json),
            ]
            run(diff_cmd)

if __name__ == "__main__":
    main()
