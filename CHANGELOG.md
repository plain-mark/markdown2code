# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.3.1] - 2024-11-20

### Fixed
- Directory structure handling in file paths
  - Properly creates nested directories from file paths
  - Correctly extracts paths from code block headers
  - Fixed handling of "filename:" prefix in paths
  - Improved directory creation before file writing

## [2.3.0] - 2024-11-20

### Added
- Web interface for markdown2code
  - Flask-based web application
  - Direct markdown content input
  - File upload support
  - Real-time conversion feedback
  - Clean, responsive UI
  - Automatic project.md file creation
  - JSON response with conversion results
  - Error handling and display

### Changed
- Added web directory with standalone Flask application
- Enhanced project structure for web support
- Updated requirements management

## [2.2.0] - 2024-11-20

### Added
- Quick restore functionality with --restore flag
  - Automatically finds most recent backup
  - Simple one-command restore
  - Lists restored files
  - Clear status reporting
- Enhanced backup management
  - Last backup detection
  - Chronological backup sorting
  - Improved backup selection

### Changed
- Improved restore workflow
- Enhanced backup listing
- Better error messages
- Clearer restore feedback

### Fixed
- Backup sorting logic
- Restore status reporting
- Error handling in restore process

## [2.1.0] - 2024-11-20

### Added
- Automatic backup feature with --backup flag
  - Creates Git backup before conversion
  - Shows backed up files
  - Displays backup branch name
  - Provides restore instructions
- Enhanced conversion workflow
  - Backup status reporting
  - Directory creation logging
  - Clear backup references
  - Restore guidance on failure

### Changed
- Improved conversion process
  - Added backup status checks
  - Enhanced directory creation feedback
  - Better error handling with backup info
- Updated CLI help messages
- Enhanced logging output

### Fixed
- Directory creation feedback
- Error handling with backups
- Status reporting clarity

## [2.0.0] - 2024-11-20

### Added
- Git-based backup system
  - Create backups with custom messages
  - List available backups
  - Restore from backups
  - Delete backups
  - View backup information
- New CLI subcommand structure
  - `markdown2code convert` for main functionality
  - `markdown2code backup` for backup operations
- Backup features:
  - Automatic branch creation
  - File-specific backups
  - Timestamp-based naming
  - Clean restore process
  - Detailed backup information

### Changed
- Major CLI interface restructuring
  - Moved main functionality to 'convert' subcommand
  - Added 'backup' subcommand group
  - Updated all command-line options
- Enhanced error handling for all operations
- Improved logging system
- Updated documentation structure

### Security
- Safe backup restoration process
- Clean working directory verification
- Git operation safety checks

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
