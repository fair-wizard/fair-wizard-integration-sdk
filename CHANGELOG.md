# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


## [1.1.0] (2026-06-05)

### Added

- `externalId` and `externalLabel` fields in the authorized user response

### Changed

- Make `firstName`, `lastName`, and `email` optional in the authorized user response
- Read OpenID claims (`given_name`, `family_name`, `email`) defensively to avoid crashes when a claim is missing

## [1.0.2] (2025-10-07)

### Fixed

- Fix crash when returning user groups in OpenID and SAML automations

## [1.0.1] (2024-11-12)

### Fixed

- Package installation on ReadTheDocs (documentation deployment)

## [1.0.0] (2024-11-05)

### Added

- Initial FAIR Wizard Integration SDK project
- Automation: *OpenID User Logged In*
- Automation: *SAML User Logged In*


[Unreleased]: /../../compare/main...develop
[1.1.0]: /../../compare/v1.0.2...v1.1.0
[1.0.2]: /../../compare/v1.0.1...v1.0.2
[1.0.1]: /../../compare/v1.0.0...v1.0.1
[1.0.0]: /../../tree/v1.0.0
