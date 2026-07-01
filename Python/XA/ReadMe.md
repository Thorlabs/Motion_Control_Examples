# Thorlabs XA Python SDK

This repository provides **source visibility and example usage** for the Thorlabs XA Python SDK.

The intent of this repository is **inspection, understanding, and reproducible builds**.

---

## Repository Layout

At the top level, the repository is organised into the SDK source and a set of **device‑specific example folders**:

```text
.
├─ xa_source/
│  ├─ src/
│  │  └─ thorlabs_xa/
│  │     ├─ interfaces/
│  │     ├─ implementations/
│  │     ├─ native_sdks/
│  │     ├─ products/
│  │     └─ shared/
│  ├─ setup.py
│  ├─ pyproject.toml
│  └─ VERSION
│
├─ KPC101/
│  └─ kpc101_test_script.py
│
├─ KDC101/
│  └─ kdc101_test_script.py
│
├─ LTS/
│  └─ linear_translation_stage_test_script.py
|
|- ...
│
└─ README.md
```

---

## Package Source Folder

The `xa_source` directory contains the **complete Python SDK package**:

- Public interfaces defined using `typing.Protocol`
- Concrete implementations that wrap the native XA SDK
- Device feature groups and device classes
- ctypes bindings and native library loading
- Packaging and build configuration (`setup.py`, `pyproject.toml`)

This directory can be built or installed as a standard Python package.

---

## Building The SDK

All build and install actions should be performed **from the `xa_source` directory**.

Before starting a build, place the native binary **tlmc_xa_native.dll** specific to your build platform in the __thorlabs_sdk__ folder. This can be obtained from the Thorlabs XA software install folder on your system.

### Editable Install (Recommended For Inspection)

```bash
pip install -e .
```

This installs the SDK in editable mode and allows the example scripts to directly import the local source.

### Build A Wheel

```bash
python -m build
```

---

## Example Scripts

The folders at the same level as `xa_source` (`KPC101`, `KDC101`, `LTS`, etc.) contain **stand‑alone example scripts**. Each folder corresponds to a specific device and demonstrates typical SDK usage.

All example scripts are intentionally written to:

- Use real hardware if detected
- Automatically fall back to **simulation mode** if no hardware is available

### Purpose

Demonstrates usage of typical device API calls including e.g.:

- Device discovery and simulation creation
- Enabling the device
- Parameter configuration
- For appropriate devices commands such as jog, home, absolute, and relative motion commands
- Limit switch and digital output configuration
- Queries for device status

**Running an example:**

```bash
python kdc101_test_script.py
```
## Summary

- `xa_source/` contains the full Python SDK and build system
- `KPC101/`, `KDC101/`, `LTS/`, etc. contain device‑specific example scripts
- Examples support both real hardware and simulation mode
- This repository is provided for **visibility and understanding** of the SDK design and usage

Official support, updates, and releases should follow Thorlabs’ standard distribution channels.
