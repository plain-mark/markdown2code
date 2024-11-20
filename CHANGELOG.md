# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.0] - 2024-01-09

### Added
- Comprehensive use case documentation
- Detailed AI chat conversion examples:
  - React Todo App example
  - Python script example
  - Configuration files example
- New sections in README:
  - AI Chat Development Sessions
  - Documentation to Implementation
  - Tutorial Creation
  - Project Templates
- Step-by-step conversion guides
- Real-world application examples

### Changed
- Enhanced README structure
- Improved usage documentation
- Updated example formats
- Clearer installation instructions

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- Documentation clarity
- Example formatting

### Security
- N/A

## [0.4.0] - 2024-01-09

### Added
- Comprehensive test suite
  - Unit tests for MarkdownConverter
  - CLI interface tests
  - File conflict handling tests
  - Preview functionality tests
- Test fixtures and helpers
- Coverage reporting with pytest-cov
- Testing documentation

### Changed
- Updated requirements.txt with test dependencies
- Enhanced error handling for better testing
- Improved code organization for testability

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- Edge cases discovered during testing
- Error handling improvements

### Security
- Added tests for file permission handling

## [0.3.0] - 2024-01-09

### Added
- Preview functionality with --preview flag
- File conflict detection and handling
- Force overwrite option with --force flag
- Detailed preview output showing:
  - Files to be created
  - Existing files that would be overwritten
  - Directory structure changes
- Enhanced documentation for file conflict handling
- Clear warning messages for existing files

### Changed
- Improved CLI interface with new flags
- Enhanced error handling for file conflicts
- Updated documentation with conflict resolution examples
- More informative status messages during conversion

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- File overwrite protection
- Directory creation safety checks

### Security
- Added checks for file system modifications

## [0.2.0] - 2024-01-09

### Added
- Modern build system configuration with pyproject.toml
- Comprehensive package metadata in setup.cfg
- Development dependencies in requirements.txt
- Test configuration for pytest
- Code formatting configuration with black
- Universal wheel support

### Changed
- Simplified setup.py to use setuptools configuration
- Moved package metadata to setup.cfg
- Updated build requirements

### Deprecated
- N/A

### Removed
- Redundant configuration from setup.py

### Fixed
- Build system dependencies specification
- Package metadata organization

### Security
- N/A

## [0.1.0] - 2024-01-09

### Added
- Initial project setup
- Core markdown to code conversion functionality
  - Support for multiple programming languages
  - Automatic file naming based on language
  - Directory structure creation from markdown
  - Comment-based filename detection
- Command-line interface
- PyPI package structure
- Executable script installation

### Changed
- Integrated generate.py functionality into modular package structure
- Standardized CLI interface

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A
