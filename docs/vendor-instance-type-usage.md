# `--vendor` and `--instance-type` Usage Guide

## Overview
This tool can derive the target ISA (`--march`) from a cloud **vendor** and **instance type**. This is useful when you know the deployment environment (e.g., AWS instance / GCP instance / AliCloud instance) and want the scanner to automatically select the appropriate target architecture.

- `--vendor` inputs the cloud provider.
- `--instance-type` inputs the instance type under that vendor.

---

## Usage

```bash
python3 -m <scanner_name> --vendor <VENDOR> --instance-type <INSTANCE> {scan_path}
```

You can also combine this with Git scanning arguments:

```bash
python3 -m <scanner_name> \
  --git-repo https://github.com/example/repo.git \
  --branch <BRANCH> \
  --vendor <VENDOR> \
  --instance-type <INSTANCE> \
  {scan_path}
```

## Option Reference

### --vendor `<VENDOR>`
Specifies the cloud vendor used to interpret `--instance-type`.

- **Supported Vendors**:
    - `AWS`, `GCP`, `AliCloud`
- **Case sensitivity** (must match a supported vendor exactly)
- Optional, **Required** when `--instance-type` is used

### --instance-type `<INSTANCE>`
Specifies the **cloud instance type** used to derive the target ISA (`--march`).

- **Supported Instance types per Vendor**:
    - AWS: `c6g`, `c7g`, `c8g`, `m6g`, `m7g`, `m8g`, `r6g`, `r7g`, `r8g`, `t4g`, `x2gd`
    - GCP: `c4a`,`n4a`, `a4x`, `t2a`
    - AliCloud: `c8y`, `c6r`, `g8y`, `g6r`, `r8y`
- **Case insensitivity** (the tool lowercases the input before matching)
- Optional, but if provided it requires `--vendor`

---

## Behavioral Rules

1. The `--vendor` and `--instance-type` options determine the value of `--march`, overriding any user-specified `-march`.
2. Specifying `--vendor` without `--instance-type` results in using the default `armv8-a` architecture.
3. If the derived ISA is not supported, the `armv8-a` architecture is used by default.

---

## Supported List

```bash
python3 -m <scanner_name> --help
# or
python3 -m <scanner_name> --h
```
Check the **Supported Vendors** and **Supported Instance Types per Vendor** sections in the help output.

---
