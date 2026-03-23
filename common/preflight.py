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

#!/usr/bin/env python3
"""
Pre-flight check for migrate-ease.
Verifies all prerequisites and Python dependencies are installed correctly.
"""

import os
import sys
import shutil
import subprocess
import platform
import importlib
import re

MIN_PYTHON = (3, 6, 8)
IS_WIN = sys.platform == "win32"
IS_MAC = sys.platform == "darwin"
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Map pip package names → importable module names
# (only for packages where they differ)
IMPORT_MAP = {
    "ruamel_yaml":      "ruamel.yaml",
    "pycryptodome":     "Crypto",
    "gitpython":        "git",
    "python-magic":     "magic",
    "python-magic-bin": "magic",
    "progressbar33":    "progressbar",
}

_pass = _fail = _warn = 0

def log_fail(msg, hint=None):
    global _fail; _fail += 1
    print("  [FAIL] {}".format(msg))
    if hint:
        for ln in hint.strip().splitlines():
            print("         {}".format(ln))



def log_warn(msg, hint=None):
    global _warn; _warn += 1
    print("  [WARN] {}".format(msg))
    if hint:
        for ln in hint.strip().splitlines():
            print("         {}".format(ln))


def check_python_version():
    """Python >= 3.6.8 is required by the project."""
    v = sys.version_info
    ver = "{}.{}.{}".format(v.major, v.minor, v.micro)
    if (v.major, v.minor, v.micro) < MIN_PYTHON:
        log_fail(
            "Python {} found — need >= {}.".format(
                ver, ".".join(str(x) for x in MIN_PYTHON)),
            "Download from https://www.python.org/downloads/"
        )


def check_pip():
    """pip must be available inside the current environment."""
    try:
        out = subprocess.check_output(
            [sys.executable, "-m", "pip", "--version"],
            stderr=subprocess.STDOUT,
        ).decode().strip()
    except Exception:
        log_fail(
            "pip is not available in this Python environment.",
            "python -m ensurepip --upgrade\n"
            "  or reinstall Python with the pip option enabled."
        )


def check_git():
    """git is needed to clone repositories for scanning."""
    git_bin = shutil.which("git")
    if not git_bin:
        if IS_WIN:
            log_fail(
                "git not found on PATH.",
                "Download Git for Windows: https://git-scm.com/download/win"
            )
        elif IS_MAC:
            log_fail(
                "git not found on PATH.",
                "Install with Homebrew:\n"
                "  brew install git"
            )
        else:
            log_fail(
                "git not found on PATH.",
                "Install with your package manager:\n"
                "  Ubuntu/Debian:  sudo apt-get install git\n"
                "  CentOS/RHEL:    sudo yum install git\n"
                "  Fedora/Anolis:  sudo dnf install git"
            )


def check_libmagic():
    """
    python-magic wraps libmagic.
    On Linux libmagic is a system library;
    On Windows python-magic-bin bundles the DLL, the two pip packages conflict if both are installed.
    On MacOS, libmagic is not included by default, it must be installed separately.
    """

    # 1. Can we import the module at all?
    try:
        import magic
    except ImportError as exc:
        if IS_WIN:
            log_fail(
                "Cannot import 'magic': {}".format(exc),
                "Run:\n"
                "  pip uninstall python-magic python-magic-bin -y\n"
                "  pip install python-magic-bin"
            )
        elif IS_MAC:
            log_fail(
                "Cannot import 'magic': {}".format(exc),
                "1. Install the system libmagic library:\n"
                "   brew install libmagic\n"
                "2. Then install the Python wrapper:\n"
                "   pip install python-magic"
            )
        else:
            log_fail(
                "Cannot import 'magic': {}".format(exc),
                "1. Install the system library:\n"
                "   Ubuntu/Debian:  sudo apt-get install libmagic1\n"
                "   CentOS/RHEL:    sudo yum install file-libs\n"
                "   Fedora/Anolis:  sudo dnf install file-libs\n"
                "2. Then:  pip install python-magic"
            )
        return

    # 2. Does the native library actually load?
    test_file = os.path.abspath(__file__)
    try:
        with open(test_file, "rb") as f:
            buf = f.read(512)   # read a chunk of the file
        result = magic.from_buffer(buf)
    except Exception as exc:
        if IS_WIN:
            log_fail(
                "magic.from_buffer() failed: {}".format(exc),
                "python-magic and python-magic-bin are probably both\n"
                "installed and conflict with each other.  Fix:\n"
                "  pip uninstall python-magic python-magic-bin -y\n"
                "  pip install python-magic-bin"
            )
        elif IS_MAC:
            log_fail(
                "magic.from_buffer() failed on macOS: {}".format(exc),
                "libmagic is required on macOS and not included by default.\n"
                "Fix:\n"
                "   brew install libmagic\n"
                "   pip install --upgrade python-magic"
            )
        else:
            log_fail(
                "magic.from_buffer() failed: {}".format(exc),
                "The system libmagic library may be missing.\n"
                "  Ubuntu/Debian:  sudo apt-get install libmagic1 file\n"
                "  CentOS/RHEL:    sudo yum install file-libs\n"
                "  Fedora/Anolis:  sudo dnf install file-libs"
            )

    # 3. Warn about conflicting installs
    try:
        pip_out = subprocess.check_output(
            [sys.executable, "-m", "pip", "list", "--format=columns"],
            stderr=subprocess.DEVNULL,
        ).decode()
        has_pm  = bool(re.search(r"^python-magic\s", pip_out, re.M))
        has_pmb = bool(re.search(r"^python-magic-bin\s", pip_out, re.M))
        if has_pm and has_pmb:
            log_fail(
                "Both python-magic AND python-magic-bin are installed.",
                "They share the same 'magic' namespace and conflict.\n"
                "Keep only one:\n"
                "  Linux/macOS:   pip uninstall python-magic-bin -y\n"
                "  Windows: pip uninstall python-magic -y"
            )
    except Exception:
        pass

def _marker_applies(marker_str):
    """
    Very small evaluator for sys_platform markers in requirements.
    e.g.  "sys_platform != 'win32'"
    """
    m = re.match(
        r"""\s*sys_platform\s*(==|!=)\s*['\"](\w+)['\"]""", marker_str
    )
    if not m:
        return True
    op, val = m.group(1), m.group(2)
    if op == "==":
        return sys.platform == val
    return sys.platform != val

def _pip_show_installed(dist_name):
    try:
        subprocess.check_output(
            [sys.executable, "-m", "pip", "show", dist_name],
            stderr=subprocess.DEVNULL,
        )
        return True
    except Exception:
        return False

def check_requirements(req_path):
    """
    Checks dependencies declared in requirements.txt by attempting imports.
    If any are missing, prints a clear error with an install command and exits(1).
    """
    if not os.path.isfile(req_path):
        log_warn("File not found: {}".format(req_path))
        return

    missing = []
    with open(req_path, "r") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue

            # Handle environment markers  (e.g. "; sys_platform != 'win32'")
            if ";" in line:
                pkg_part, marker = line.split(";", 1)
                if not _marker_applies(marker):
                    continue          # this line is not for our platform
                line = pkg_part.strip()

            # Strip version specifiers
            pkg_name = re.split(r"[~=><!]", line)[0].strip().lower()
            if not pkg_name:
                continue

            if pkg_name in ("python-magic", "python-magic-bin"):
                if not _pip_show_installed(pkg_name):
                    # Special case for python-magic: the package is named python-magic but the module is magic
                    # We want to report it as missing if neither python-magic nor python-magic-bin is installed
                    log_fail("{} — not installed".format(pkg_name))
                    missing.append(pkg_name)
                continue

            import_name = IMPORT_MAP.get(pkg_name, pkg_name)
            try:
                importlib.import_module(import_name)
            except ImportError:
                log_fail("{} — not installed".format(pkg_name))
                missing.append(pkg_name)

    if missing:
        print("\n  Install missing packages with:")
        print("      pip install -r {}".format(req_path))


def check_python_packages():
    """Parse and verify the root requirements.txt."""
    check_requirements(os.path.join(PROJECT_ROOT, "requirements.txt"))


def check_pythonpath():
    """PYTHONPATH must include the project root for scanners to work."""
    pp = os.environ.get("PYTHONPATH", "")
    parts = [os.path.normcase(os.path.abspath(p))
             for p in pp.split(os.pathsep) if p]
    root_norm = os.path.normcase(os.path.abspath(PROJECT_ROOT))

    if root_norm not in parts:
        if IS_WIN:
            hint = '$env:PYTHONPATH="{}"'.format(PROJECT_ROOT)
        else:
            hint = 'export PYTHONPATH={}'.format(PROJECT_ROOT)
        log_fail(
            "PYTHONPATH does not include the project root.",
            "Set it before running scanners:\n  {}".format(hint)
        )

def preflight_dependency_check():
    check_python_version()
    check_pip()
    check_git()
    check_python_packages()
    check_libmagic()
    check_pythonpath()

    summary = "{} passed, {} failed, {} warnings".format(_pass, _fail, _warn)
    if _fail:
        print("  Pre-flight Check Failed")
        print("  Platform : {} {} ({})".format(
        platform.system(), platform.release(), platform.machine()))
        print("  " + summary)
        sys.exit(1)
