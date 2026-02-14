"""
Copyright 2025 Google LLC

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

import unittest

from common.arch_strings import ARMV8_0, ARMV9_0, ARMV9_2
from common.main import PLATFORM_CONFIG, SUPPORTED_VENDORS, get_supported_instance_types, get_isa_for_instance_type


class TestMain(unittest.TestCase):

    def test_supported_vendors(self):
        self.assertIn("AWS", SUPPORTED_VENDORS)
        self.assertIn("GCP", SUPPORTED_VENDORS)
        self.assertEqual(len(SUPPORTED_VENDORS), 2)

    def test_get_supported_instance_types(self):
        aws_instances = get_supported_instance_types("AWS")
        self.assertIn("Graviton", aws_instances)
        self.assertEqual(len(aws_instances), 1)

        gcp_instances = get_supported_instance_types("GCP")
        self.assertIn("C4A", gcp_instances)
        self.assertIn("N4A", gcp_instances)
        self.assertEqual(len(gcp_instances), 2)

        self.assertEqual(get_supported_instance_types("NonExistentVendor"), [])

    def test_get_isa_for_instance_type(self):
        self.assertEqual(get_isa_for_instance_type("AWS", "Graviton"), ARMV8_0)
        self.assertEqual(get_isa_for_instance_type("GCP", "C4A"), ARMV9_0)
        self.assertEqual(get_isa_for_instance_type("GCP", "N4A"), ARMV9_2)

        self.assertIsNone(get_isa_for_instance_type("AWS", "NonExistentInstance"))
        self.assertIsNone(get_isa_for_instance_type("NonExistentVendor", "C4A"))


if __name__ == '__main__':
    unittest.main()
