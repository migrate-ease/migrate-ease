#!/usr/bin/python3
"""
Copyright 2017-2025 Arm ltd.

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


def main(argv=None) :
    """
    Entry point for: python -m java

    Keep compatibility with the existing layout where 'advisor' is imported
    as a top-level module by adding the package directory to sys.path.
    """
    # Keep existing behavior: allow "from advisor import main"
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))

    # If called programmatically, allow passing argv.
    if argv is not None:
        sys.argv = [sys.argv[0], *argv]

    from advisor import main as advisor_main

    advisor_main.main()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
