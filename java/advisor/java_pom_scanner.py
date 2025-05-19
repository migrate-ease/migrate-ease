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

import os
import re
import time
from lxml import etree


from common.localization import _ as i18n
from common.report_factory import ReportOutputFormat
from common.checkpoint import init_checkpoints, Checkpoint

from .java_scanner import JavaScanner
from .java_pom_issue import JavaPomIssue

class JavaPomScanner(JavaScanner):

    AARCH64_INCOMPATILE_ARTIFACTS = []

    def __init__(self, output_format, march):
        self.output_format = output_format
        self.march = march

        self.with_highlights = bool(
            self.output_format == ReportOutputFormat.HTML or self.output_format == ReportOutputFormat.JSON)
        self.load_checkpoints()

    def accepts_file(self, filename):
        return os.path.basename(filename) == 'pom.xml'

    def load_checkpoints(self):
        super().load_checkpoints()

        start_time = time.time()
        #  Checkpoints for artifacts that don't work on aarch64
        self.AARCH64_INCOMPATILE_ARTIFACTS = init_checkpoints(
            self.checkpoints_content['AARCH64_INCOMPATILE_ARTIFACTS'],
            None
        )
        # please remember to remove lines for profiling after optimizing :)
        end_time = time.time()

        print('[Java] Initialization of checkpoints took %f seconds.' % (end_time - start_time))

    def get_dependencies(self, file_path):
        try:
            tree = etree.parse(file_path, etree.XMLParser(remove_comments=True))
            root = tree.getroot()

            # Define the namespace for Maven POM
            namespaces = {'m': 'http://maven.apache.org/POM/4.0.0'}

            # Get properties as dependencies may refer some of them
            properties = {}
            properties_section = root.find(".//m:properties", namespaces)
            if properties_section is not None:
                for this_prop in properties_section:
                    properties[this_prop.tag.split('}')[-1]] = this_prop.text

            # Find all dependencies
            dependency_list = []
            dependencies = root.findall('.//m:dependency', namespaces)
            for this_dep in dependencies:
                group_id = this_dep.find('m:groupId', namespaces)
                artifact_id = this_dep.find('m:artifactId', namespaces)
                version = this_dep.find('m:version', namespaces)

                group_id = group_id.text if group_id is not None else "N/A"
                artifact_id = artifact_id.text if artifact_id is not None else "N/A"
                version = version.text if version is not None else "N/A"

                # skip invalid dependency
                if group_id == 'N/A':
                    continue

                # group_id/artifact_id/version may refer certain properties
                # example: apache/spark/pom.xml
                #   <groupId>${hive.group}</groupId>
                #   <artifactId>hive-beeline</artifactId>
                #   <version>${hive.version}</version>
                #   <scope>${hive.deps.scope}</scope>
                if group_id and re.search(r'\$\{[^}]+\}', group_id):
                    property_keys = re.findall(r'\$\{(.*?)\}', group_id)
                    for k in property_keys:
                        v = properties.get(k, f"UNRESOLVED({k})")
                        pattern = r'\$\{' + re.escape(k) + r'\}'
                        group_id = re.sub(pattern, v, group_id)

                if artifact_id and re.search(r'\$\{[^}]+\}', artifact_id):
                    property_keys = re.findall(r'\$\{(.*?)\}', artifact_id)
                    for k in property_keys:
                        v = properties.get(k, f"UNRESOLVED({k})")
                        pattern = r'\$\{' + re.escape(k) + r'\}'
                        artifact_id = re.sub(pattern, v, artifact_id)

                if version and re.search(r'\$\{[^}]+\}', version):
                    property_keys = re.findall(r'\$\{(.*?)\}', version)
                    for k in property_keys:
                        v = properties.get(k, f"UNRESOLVED({k})")
                        pattern = r'\$\{' + re.escape(k) + r'\}'
                        version = re.sub(pattern, v, version)

                # Add dependency details to the list
                dependency_list.append({
                    "groupId": group_id,
                    "artifactId": artifact_id,
                    "version": version,
                    "line": this_dep.sourceline
                })

            return dependency_list

        except etree.XMLSyntaxError as e:
            print(f"Error parsing the POM file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return []

    def scan_file_object(self, filename, file_obj, report):

        _lines = file_obj.readlines()
        self.FILE_SUMMARY[self.POM]['count'] += 1
        self.FILE_SUMMARY[self.POM]['loc'] += len(_lines)

        issues = []
        lines = {}
        match = False

        # parse pom to get dependencies list and versions
        dependencies = self.get_dependencies(filename)

        c: Checkpoint
        # iterate dependencies
        for this_dep in dependencies:
            # check using data from check_points.yaml
            artifact = this_dep['groupId']+'.'+this_dep['artifactId']+'.'+this_dep['version']
            for c in self.AARCH64_INCOMPATILE_ARTIFACTS:
                match = c.pattern_compiled.search(artifact)
                if match:
                    issues.append(JavaPomIssue(filename,
                                                lineno=this_dep['line'],
                                                checkpoint=c.pattern,
                                                description='' if not c.help else '\n' + c.help))

        for issue in issues:
            issue.set_code_snippet(issue.get_code_snippets(lines=lines, with_highlights=self.with_highlights))
            report.add_issue(issue)

    def finalize_report(self, report):
        pass
