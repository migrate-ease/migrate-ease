"""
Copyright 2020-2023 Alibaba Inc.

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
import re
import time

import requests
from typing import Tuple

from common.arch_strings import NON_AARCH64_ARCHS, SUPPORTED_MARCH
from common.continuation_parser import ContinuationParser
from common.naive_comment_parser import NaiveCommentParser
from common.report_factory import ReportOutputFormat
from common.checkpoint import init_checkpoints

from .configuration_info_issue import ConfigurationInfoIssue
from .docker_scanner import DockerScanner
from .image_issue import ImageIssue
from .naive_dockerfile import NaiveDockerfile, PreprocessorDirective
from .plugin_issue import PluginIssue


class DockerfileScanner(DockerScanner):
    """
    Scanner that scans dockerfiles for potential porting issues
    """

    DOCKERFILE_SOURCE = ['Dockerfile', 'dockerfile']

    NON_AARCH64_RE = re.compile(r'.*(%s).*' % '|'.join([(r'%s' % x) for x in NON_AARCH64_ARCHS]))

    AARCH64_INCOMPATIBLE_EXTENSION_PACKAGES = []

    def __init__(self, output_format, march):
        self.output_format = output_format
        self.march = march

        self.with_highlights = bool(
            self.output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)
        self.load_checkpoints()

    def load_checkpoints(self):
        super().load_checkpoints()

        start_time = time.time()

        self.AARCH64_INCOMPATIBLE_EXTENSION_PACKAGES = init_checkpoints(
            self.checkpoints_content['X86_PYTHON_EXTENSION_PACKAGES'],
            self.checkpoints_content["AARCH64_PYTHON_EXTENSION_PACKAGES"] +
            self.checkpoints_content["COMMON_AARCH64_AND_X86_PYTHON_EXTENSION_PACKAGES"]
        )

        # please remember to remove lines for profiling after optimizing :)
        end_time = time.time()

        print('[Docker] Initialization of checkpoints took %f seconds.' % (end_time - start_time))

    def accepts_file(self, filename):

        ext = os.path.basename(filename)
        # allow to check Dockfile in different naming format like:
        # Dockerfile.debug, Dockerfile.release
        # worker.Dockerfile, tests.dockerfile
        ext = ext.lower().split('.')
        return 'dockerfile' in ext

    def parse_image_name(self, image_string: str) -> Tuple[str, str, str]:
        # Parse image name string to <registry>/<repository>:<tag>
        # registry and tag are optional, repository = <namespace>/<image> or library/<image>
        # Default values for optional fields
        registry = "registry-1.docker.io"
        repository = ""
        tag = "latest"

        parts = image_string.split('/', 1)
        if '.' in parts[0]:
            # A registry is given
            registry = parts[0]
            parts.pop(0)
            repository = parts[0]
        else:
            repository = "/".join(parts)

        if '/' not in repository:
            # An official image is specified
            repository = f"library/{repository}"

        if ':' in repository:
            # A tag is specified
            repository, tag = repository.rsplit(':', 1)

        return registry, repository, tag

    def check_arm64_support(self, registry, repo, tag):
        supported = False
        if registry == "registry-1.docker.io":
            # For docker hub, use a simple way to check
            tag_info_url = f"https://hub.docker.com/v2/repositories/{repo}/tags/{tag}/"
            try:
                response = requests.get(tag_info_url)
                response.raise_for_status()
                # Parse the JSON output
                data = response.json()
                for image in data.get('images', []):
                    if image['architecture'] == "arm64":
                        supported = True
                        break
            except Exception as err:
                print(f"An error occurred: {err}")
        else:
            # Other registry
            # Follow APIs defined at https://github.com/distribution/distribution/blob/main/docs/content/spec/api.md and https://github.com/distribution/distribution/blob/main/docs/content/spec/auth/token.md
            registry_base_url = f"https://{registry}/v2/"

            # Get URL for requesting access token
            response = requests.get(registry_base_url)
            if response.status_code == 401:
                for key, value in response.headers.items():
                    if 'www-authenticate' == key.lower():
                        auth_scheme = "Bearer" # See https://datatracker.ietf.org/doc/html/rfc6750#section-3
                        realm = re.search(r'realm="([^"]+)"', value).group(1)
                        service = re.search(r'service="([^"]+)"', value).group(1)

                try:
                    # Get access token
                    token_url = f"{realm}?service={service}&scope=repository:{repo}:pull"
                    response = requests.get(token_url)
                    response.raise_for_status()
                    data = response.json()
                    access_token = data['access_token']

                    # Query manifest with tag
                    tag_info_url = f"https://{registry}/v2/{repo}/manifests/{tag}"
                    headers = {
                        'Authorization': f"Bearer {access_token}",
                        'Accept': 'application/vnd.docker.distribution.manifest.list.v2+json'
                    }
                    response = requests.get(tag_info_url, headers=headers)
                    response.raise_for_status()

                    # Parse the JSON output
                    data = response.json()
                    for image in data.get('manifests', []):
                        if image['platform']['architecture'] == "arm64":
                            supported = True
                            break
                except requests.exceptions.HTTPError as http_err:
                    print(f"HTTP error occurred: {http_err} ")
                except Exception as err:
                    print(f"An error occurred: {err}")

        return supported

    def scan_file_object(self, filename, file_obj, report):

        _lines = file_obj.readlines()
        ext = os.path.basename(filename)
        ext = ext.lower().split('.')

        if 'dockerfile' in ext:
            self.FILE_SUMMARY[self.DOCKERFILE]['count'] += 1
            self.FILE_SUMMARY[self.DOCKERFILE]['loc'] += len(_lines)

        continuation_parser = ContinuationParser()
        naive_dockerfile = NaiveDockerfile(march=self.march)
        comment_parser = NaiveCommentParser()

        if self.march in SUPPORTED_MARCH:
            PACKAGE_CHECKPOINTS = self.AARCH64_INCOMPATIBLE_EXTENSION_PACKAGES
            ARCH_RE = self.NON_AARCH64_RE
        else:
            raise RuntimeError('unknown target processor architecuture: %s.' % self.march)

        issues = []  # type: List[Issue]
        lines = {}

        for lineno, line in enumerate(_lines, 1):
            lines[lineno] = line

        for lineno in lines.keys():

            line = lines[lineno]

            line = continuation_parser.parse_line(line)
            if not line:
                continue

            is_comment = comment_parser.parse_line(line)
            if is_comment:
                continue

            result = naive_dockerfile.parse_line(line)  # type: PreprocessorDirective

            # FROM
            if result.directive_type == PreprocessorDirective.TYPE_FROM:

                parts = line.strip(result.directive_type)
                base_img = re.search(r'^\s+([^\s]+)', parts).group().lstrip()
                if '$' in base_img:
                    issues.append(ImageIssue(filename,
                                         lineno,
                                         march=self.march,
                                         image=parts,
                                         checkpoint=None))
                else:
                    registry, repo, tag = self.parse_image_name(base_img)
                    if False == self.check_arm64_support(registry, repo, tag):
                        issues.append(ImageIssue(filename,
                                         lineno,
                                         march=self.march,
                                         image=parts,
                                         checkpoint=None))

            # RUN/CMD/ENTRYPOINT
            elif result.directive_type in PreprocessorDirective.TYPE_EXEC_COMMAND:

                # python package check
                for c in PACKAGE_CHECKPOINTS:

                    match = c.pattern_compiled.search(line)
                    if match:
                        issues.append(PluginIssue(filename,
                                                  lineno,
                                                  march=self.march,
                                                  plugin=c.pattern,
                                                  checkpoint=c.pattern,
                                                  description='' if not c.help else '\n' + c.help))

            # ENV/ARG/LABEL
            elif result.directive_type in PreprocessorDirective.TYPE_OTHER_COMMAND:

                match = ARCH_RE.search(line)
                if match:
                    issues.append(ConfigurationInfoIssue(filename,
                                                         lineno,
                                                         march=self.march,
                                                         checkpoint=line,
                                                         description=None))

        #  to extract code snippets
        for issue in issues:
            issue.set_code_snippet(issue.get_code_snippets(lines, with_highlights=self.with_highlights))
            report.add_issue(issue)
