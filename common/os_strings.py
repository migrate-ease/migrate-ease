"""
Copyright 2020-2023 Alibaba Inc.
Copyright 2017-2020 Arm Ltd.

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

# NOTE
# ---
# This file defines OS specific information including supported OS and not
# supported OS.

WINDOWS = []
LINUX = []
MACOS = []

_SUPPORTED_OS = {
    'Linux':
    {
        'AliOS':
        {
            'supported': True,
            'kernel': ''
        },
        'OpenAnolis':
        {
            'supported': True,
            'kernel': ''
        },
        'CentOS 7.4':
        {
            'supported': True,
            'kernel': ''
        },
        'CentOS 7.5':
        {
            'supported': True,
            'kernel': ''
        },
        'CentOS 7.6':
        {
            'supported': True,
            'kernel': ''
        },
        'CentOS 7.7':
        {
            'supported': True,
            'kernel': ''
        },
        'CentOS 8.0':
        {
            'supported': True,
            'kernel': ''
        },
        'CentOS 8.1':
        {
            'supported': True,
            'kernel': ''
        },
        'CentOS 8.2':
        {
            'supported': True,
            'kernel': ''
        },
        'Kylin V10 SP1':
        {
            'supported': False,
            'kernel': ''
        },
        'NeoKylin V7U5':
        {
            'supported': False,
            'kernel': ''
        },
        'NeoKylin V7U6':
        {
            'supported': False,
            'kernel': ''
        },
        'UOS 20 SP1':
        {
            'supported': False,
            'kernel': ''
        }
    }
}
DEFAULT_OS = 'OpenAnolis'
SUPPORTED_OS = [_ for _ in list(_SUPPORTED_OS['Linux'].keys()) if _SUPPORTED_OS['Linux'][_]['supported']]
