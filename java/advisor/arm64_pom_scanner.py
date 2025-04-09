"""
Copyright 2017-2025 Arm Ltd.

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
from .java_pom_scanner import JavaPomScanner


class Arm64PomScanner(JavaPomScanner):

    """
    Scanner that scans binaries in a JAR for ARM64 potential
    porting issues.
    """

    def __init__(self, output_format, arch, march):

        super().__init__(output_format=output_format,
                         arch=arch,
                         march=march)
