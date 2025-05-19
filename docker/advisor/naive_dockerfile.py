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


class PreprocessorDirective(object):

    """
    Information about a preprocessor directive.

    The types of directives:
    ===
    TYPE_FROM        - a FROM directive.
    TYPE_RUN         - a RUN directive.
    TYPE_CMD         - a CMD directive.
    TYPE_ENTRYPOINT  - a ENTRYPOINT directive.
    TYPE_ENV         - a ENV directive.
    TYPE_ARG         - a ARG directive.
    TYPE_LABEL       - a LABEL directive.
    TYPE_OTHER       - some other directive.
    TYPE_INVALID     - an invalid directive.
    """
    TYPE_FROM = 'FROM'
    TYPE_RUN = 'RUN'
    TYPE_CMD = 'CMD'
    TYPE_ENTRYPOINT = 'ENTRYPOINT'
    TYPE_ENV = 'ENV'
    TYPE_ARG = 'ARG'
    TYPE_LABEL = 'LABEL'
    TYPE_OTHER = 'other'
    TYPE_INVALID = 'invalid'

    TYPE_ALL = [TYPE_FROM, TYPE_RUN, TYPE_CMD, TYPE_ENTRYPOINT, TYPE_ENV, TYPE_ARG, TYPE_LABEL]
    TYPE_EXEC_COMMAND = [TYPE_RUN, TYPE_CMD, TYPE_ENTRYPOINT]
    TYPE_OTHER_COMMAND = [TYPE_ENV, TYPE_ARG, TYPE_LABEL]

    def __init__(self, directive_type):

        self.directive_type = directive_type

class NaiveDockerfile(object):

    """
    Naive dockerfile preprocessor. This class is used by DockerfileScanner to determine
    which source lines will/will not be compiled on target platforms.
    """

    def __init__(self, march: str):

        self.march = march

    def parse_line(self, line):
        # type: (str) -> Union[PreprocessorDirective]
        """
        Parse preprocessor directives in a source line.

        Args:
            line (str): The line to parse.

        Returns:
            PreprocessorDirective: Information about the parsed directive.
        """
        for x in PreprocessorDirective.TYPE_ALL:
            if line.lstrip().startswith(x):
                return self._parse_directive_line(line)
        return PreprocessorDirective(directive_type=None)

    def _parse_directive_line(self, line):
        # type: (str) -> PreprocessorDirective
        parts = line.lstrip().split(maxsplit=1)  # type: List[str]

        directive = parts[0]

        if directive == 'FROM':
            return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_FROM)

        elif directive == 'RUN':
            return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_RUN)
        
        elif directive == 'CMD':
            return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_CMD)

        elif directive == 'ENTRYPOINT':
            return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_ENTRYPOINT)

        elif directive == 'ENV':
            return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_ENV)

        elif directive == 'ARG':
            return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_ARG)

        elif directive == 'LABEL':
            return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_LABEL)

        else:
            return PreprocessorDirective(directive_type=PreprocessorDirective.TYPE_OTHER)
