# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.6.1] - 2026-09-09

### Fixed

- KIM notification ID enum fields could cause typing error due to trailing commas.

## [1.6.0] - 2026-09-08

### Added

- KIM001 product API support.

## 1.5.0 - 2026-09-08

### Added

- BBD30x product API support.
- BPC30x product API support.
- BPC301 product API support.
- BSC201 product API support.
- BSC201v4 product API support.
- KST101 product API support.
- KBD101 product API support.
- PDXC2 product API support.
- PDXC3 product API support.
- TBD001 product API support.

### Fixed

- MoveSyncArray now correctly stores time positions as an array rather than a single value.
- LTS API now exposes UniversalStatusBits API.
- Setting AuxIoPortMode now calls the correctly named function in the native API.
- Native API: PDXC2/3 now raises 'stopped' message when the device is stopped.
- UMC brushless and stepper logical channels incorrectly exposed PositionCounter functionality.

## [1.4.0] - 2026-09-02

### Added

- UMC product API support.

### Fixed

- Native API: Resolved a crash when using multiple FTDI devices simultaneously.

## [1.3.3] - 2026-08-25

### Added

- Provided stage identifier values for DDS800 and DDS1000.

### Fixed

- Native API: Improvements in the area of ethernet stability and error recovery.
- Native API: Issues with TLMC_RegisterLoggingHandler formatting resolved.
- Native API: Issues with TLMC_DiscoverEthernetDeviceInfo formatting resolved.
- Native API: Devices connected via ethernet were potentially not having their firmware level checked.
- UMC stepper logical channel incorrectly exposed disconnect functionality.

### Changed

- Native API: Internal improvements.

## [1.3.2] - 2026-08-07

### Fixed

- In the native API, PositionCounter device feature is now present for LTS and its simulation.

## [1.3.1] - 2026-07-01

### Fixed

- In the native API, simulations are now correctly filtering packets according to channel ID.

### Changed

- Internal native API improvements.
- Internal python API improvements.

## [1.2.1] - 2026-06-04

### Changed

- Resynchronize of wrapper python enumerations with those in the native API.

## [1.2.0] - 2026-06-02

### Added

- KST101 product API support.
- KST201 product API support.

## [1.1.11] - 2026-06-01

### Fixed

- In the native API, device with serial number uninitialized in HW info is now discovered.

## [1.1.10] - 2026-04-13

### Fixed

- In the native API, the conversion factor used to convert MicrostepsPerEncoderCount in StepperLoopParams is now correct.

## [1.1.9] - 2026-04-10

### Fixed

- In the native API's StepperLoopParams, MicrostepsPerEncoderCount is now a signed 32-bit integer (previously unsigned).

## [1.1.8] - 2026-04-10

### Changed

- Internal native API improvements.

## [1.1.7] - 2026-04-08

### Fixed

- Removed deflection and velocity fields from the CurrentLoopParams structure.

## [1.1.6] - 2026-03-31

### Changed

- Added GitHub changelog URL to package metadata.

## [1.1.5] - 2026-03-27

### Changed

- Internal native API improvements.

## [1.1.4] - 2026-03-26

### Changed

- Internal native API improvements.

## [1.1.3] - 2026-03-26

### Fixed

- Connected product information now correctly reported as "rotational - continuous" (rather than "rotational - fixed range") for FW103, FW6, FW12, HDR50 and NR360S stages.

## [1.1.2] - 2026-03-20

### Added

- Added native API support for PDXC3.

## [1.1.1] - 2026-03-03

### Changed

- Internal native API improvements.

## [1.1.0] - 2026-02-19

### Added

- LTS product API support.
- KDC product API support.

## [1.0.0] - 2026-01-21

### Added

- Initial python wrapper API implementation.
