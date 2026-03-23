"""
Copyright 2026 Arm ltd.

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


from common.arch_strings import *


# Define mappings for vendors, instance types, and their respective ISAs
PLATFORM_CONFIG = {
    "AWS": {
        "graviton": ARMV8_0,  # Example: Graviton uses Armv8-A
        "c6g": ARMV8_2,  # doc_link: https://aws.amazon.com/ec2/instance-types/c6g/
        "c7g": ARMV8_4,  # doc_link: https://aws.amazon.com/ec2/instance-types/c7g/
        "c8g": ARMV9_0,  # doc_link: https://aws.amazon.com/ec2/instance-types/c8g/
        "m6g": ARMV8_2,  # doc_link: https://aws.amazon.com/ec2/instance-types/m6g/
        "m7g": ARMV8_4,  # doc_link: https://aws.amazon.com/ec2/instance-types/m7g/
        "m8g": ARMV9_0,  # doc_link: https://aws.amazon.com/ec2/instance-types/m8g/
        "r6g": ARMV8_2,  # doc_link: https://aws.amazon.com/ec2/instance-types/r6g/
        "r7g": ARMV8_4,  # doc_link: https://aws.amazon.com/ec2/instance-types/r7g/
        "r8g": ARMV9_0,  # doc_link: https://aws.amazon.com/ec2/instance-types/r8g/
        "t4g": ARMV8_2,  # doc_link: https://aws.amazon.com/ec2/instance-types/t4/
        "x2gd": ARMV8_2  # doc_link: https://aws.amazon.com/ec2/instance-types/x2g/
    },
    "GCP": {
        "c4a": ARMV9_0,  # C4A uses Armv9-A, doc_link: https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series
        "n4a": ARMV9_2,  # N4A uses Armv9.2-A, doc_link: https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series
        "a4x": ARMV9_2,  # A4X uses Armv9.2-A, doc_link: https://docs.cloud.google.com/compute/docs/general-purpose-machines#a4x_series
        "t2a": ARMV8_2,  # T2A uses Armv8.2-A, doc_link: https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines
    },
    "AliCloud": {
        "c8y": ARMV8_6_SVE2,  # doc link: https://www.alibabacloud.com/help/en/ecs/user-guide/overview-of-instance-families#c8y
        "c6r": ARMV8_0,       # doc link: https://www.alibabacloud.com/help/en/ecs/user-guide/overview-of-instance-families#c6r
        "g8y": ARMV8_6_SVE2,  # doc link: https://www.alibabacloud.com/help/en/ecs/user-guide/overview-of-instance-families#g8y
        "g6r": ARMV8_0,       # doc link: https://www.alibabacloud.com/help/en/ecs/user-guide/overview-of-instance-families#g6r
        "r8y": ARMV8_6_SVE2,  # doc link: https://www.alibabacloud.com/help/en/ecs/user-guide/overview-of-instance-families#r8y
    }
}

SUPPORTED_VENDORS = list(PLATFORM_CONFIG.keys())

def get_supported_instance_types(vendor):
    return list(PLATFORM_CONFIG.get(vendor, {}).keys())

def get_isa_for_instance_type(vendor, instance_type):
    return PLATFORM_CONFIG.get(vendor, {}).get(instance_type)
