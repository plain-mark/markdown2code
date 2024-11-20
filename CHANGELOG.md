# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-11-20

### Added
- Core markdown to code conversion functionality
  - Support for multiple programming languages
  - Automatic file naming based on language
  - Directory structure creation from markdown
  - Comment-based filename detection
- Command-line interface with options:
  - Preview mode (--preview)
  - Force overwrite (--force)
  - Output directory (--output)
  - Verbose logging (--verbose)
  - Configuration file (--config)
- Configuration system with YAML support
  - User-specific configuration (~/.markdown2code.yml)
  - Project-specific configuration (.markdown2code.yml)
  - Default configuration creation (--create-config)
- Custom file naming patterns
  - Multiple patterns per language
  - Pattern fallback system
  - User-definable patterns
- Verbose logging mode
  - Detailed debug information
  - Configurable log levels
  - Structured log format
- Comprehensive test suite
  - Unit tests for core functionality
  - CLI interface tests
  - File conflict handling tests
  - Preview functionality tests
- Documentation
  - Detailed README with table of contents
  - Contributing guidelines
  - AI chat conversion examples
  - Configuration examples
  - Troubleshooting guide
- Build system
  - Modern Python packaging
  - Development dependencies
  - Test configuration
  - Universal wheel support

### Changed
- Enhanced file naming system
- Improved logging infrastructure
- Updated CLI interface
- Refactored converter for configuration support
- Reorganized documentation structure
- Improved development guidelines

### Security
- File conflict protection
- Configuration file permission checks
- Added security guidelines for contributors


## [0.8.0] - 2024-11-20

### Added
- Comprehensive table of contents in README.md
- Enhanced documentation structure:
  - Quick start guide
  - Configuration examples
  - Command line reference
  - Troubleshooting section
- Detailed menu navigation
- Configuration examples
- Common issues and solutions
- Development quick start

### Changed
- Reorganized README.md structure
- Improved documentation navigation
- Enhanced configuration documentation
- Updated troubleshooting guide

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- Documentation organization
- Navigation structure
- Configuration examples clarity

### Security
- N/A

## [0.7.0] - 2024-11-20

### Added
- Comprehensive CONTRIBUTING.md with:
  - Development setup instructions
  - Code style guidelines
  - Pull request process
  - Project structure documentation
  - Feature development guidelines
  - Release process
  - Code of conduct
- Detailed contribution workflows
- Development environment setup guide
- Testing instructions
- Release procedures

### Changed
- Enhanced project documentation structure
- Improved development guidelines
- Updated project organization

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- Documentation organization
- Development workflow clarity

### Security
- Added security guidelines for contributors


## [0.6.0] - 2024-11-20

### Added
- Configuration system with YAML support
  - User-specific configuration (~/.markdown2code.yml)
  - Project-specific configuration (.markdown2code.yml)
  - Default configuration creation (--create-config)
- Custom file naming patterns
  - Multiple patterns per language
  - Pattern fallback system
  - User-definable patterns
- Verbose logging mode
  - Detailed debug information
  - Configurable log levels
  - Structured log format
- Configuration CLI options
  - Custom config file path (--config)
  - Verbose output (--verbose)
  - Configuration generation

### Changed
- Enhanced file naming system
- Improved logging infrastructure
- Updated CLI interface with new options
- Refactored converter for configuration support

### Deprecated
- N/A

### Removed
- Hard-coded default filenames
- Basic print statements

### Fixed
- File naming conflicts with multiple files
- Logging consistency
- Configuration inheritance

### Security
- Configuration file permission checks

## [0.5.0] - 2024-11-20

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

## [0.4.0] - 2024-11-20

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


## [0.3.0] - 2024-11-20

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


## [0.2.0] - 2024-11-20

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

## [0.1.0] - 2024-11-20

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
