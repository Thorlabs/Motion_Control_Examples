# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0] - 2026-06-02

### Added

- KST101 product API support (#10003).
- KST201 product API support (#10003).

## [1.1.11] - 2026-06-01

### Fixed

- In the native API, device with serial number unitialized in HW info is now discovered (#9926).

## [1.1.10] - 2026-04-13

### Fixed

- In the native API, the conversion factor used to convert MicrostepsPerEncoderCount in StepperLoopParams is now correct (#9906).

## [1.1.9] - 2026-04-10

### Fixed

- In the native API's StepperLoopParams, MicrostepsPerEncoderCount is now a signed 32-bit integer (previously unsigned) (#9906).

## [1.1.8] - 2026-04-10

### Changed

- Internal native API improvements (#9902).

## [1.1.7] - 2026-04-08

### Fixed

- Removed deflection and velocity fields from the CurrentLoopParams structure (#9904).

## [1.1.6] - 2026-03-31

### Changed

- Added GitHub changelog URL to package metadata (#9903).

## [1.1.5] - 2026-03-27

### Changed

- Internal native API improvements (#9899).

## [1.1.4] - 2026-03-26

### Changed

- Internal native API improvements (#9895).

## [1.1.3] - 2026-03-26

### Fixed

- Connected product information now correctly reported as "rotational - continuous" (rather than "rotational - fixed range") for FW103, FW6, FW12, HDR50 and NR360S stages (#9883).

## [1.1.2] - 2026-03-20

### Added

- Added native API support for PDXC3 (#9879).

## [1.1.1] - 2026-03-03

### Changed

- Internal native API improvements (#9858).

## [1.1.0] - 2026-02-19

### Added

- LTS product API support (#9851).
- KDC product API support (#9850).

## [1.0.0] - 2026-01-21

### Added

- Initial python wrapper API implementation (#9719, #9720).