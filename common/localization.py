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

import gettext
import os

#  from advisor import __name__ as PACKAGE
PACKAGE = 'ad'

localedir = os.path.join(os.path.dirname(__file__), 'locale')
cat = gettext.Catalog(PACKAGE, localedir=localedir, fallback=True)
_ = cat.gettext
