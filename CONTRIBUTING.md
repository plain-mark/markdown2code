# Contributing to markdown2code

```bash
                       _       _                     ___               _      
                      | |     | |                   |__ \             | |     
  _ __ ___   __ _ _ __| | ____| | _____      ___ __    ) |___ ___   __| | ___ 
 | '_ ` _ \ / _` | '__| |/ / _` |/ _ \ \ /\ / / '_ \  / // __/ _ \ / _` |/ _ \
 | | | | | | (_| | |  |   < (_| | (_) \ V  V /| | | |/ /| (_| (_) | (_| |  __/
 |_| |_| |_|\__,_|_|  |_|\_\__,_|\___/ \_/\_/ |_| |_|____\___\___/ \__,_|\___|
```   

Thank you for your interest in contributing to markdown2code! This document provides guidelines and instructions for contributing to the project.

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/plain-mark/markdown2code.git
cd markdown2code
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

## Running Tests

Run the test suite using pytest:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=markdown2code
```

## Code Style

This project follows these coding standards:
- PEP 8 style guide
- Black code formatter
- Type hints where appropriate
- Docstrings for all public functions and classes

Format your code using black:
```bash
black .
```

## Making Changes

1. Create a new branch for your changes:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and ensure:
   - All tests pass
   - New features include tests
   - Documentation is updated
   - CHANGELOG.md is updated

3. Commit your changes:
```bash
git add .
git commit -m "Description of changes"
```

## Pull Request Process

1. Update documentation:
   - README.md for user-facing changes
   - Docstrings for API changes
   - CHANGELOG.md under "Unreleased" section

2. Run tests and ensure they pass:
```bash
pytest
```

3. Push your changes:
```bash
git push origin feature/your-feature-name
```

4. Create a Pull Request with:
   - Clear description of changes
   - Any related issues referenced
   - Screenshots for UI changes
   - Test results

## Project Structure

```
markdown2code/
├── markdown2code/          # Main package
│   ├── __init__.py        # Package initialization
│   ├── cli.py             # Command-line interface
│   ├── converter.py       # Core conversion logic
│   └── config.py          # Configuration handling
├── tests/                 # Test suite
│   ├── __init__.py
│   ├── test_cli.py
│   └── test_converter.py
├── CHANGELOG.md          # Version history
├── CONTRIBUTING.md       # This file
├── LICENSE              # Apache License
├── README.md            # Project documentation
├── requirements.txt     # Dependencies
├── setup.cfg           # Package configuration
├── setup.py            # Build configuration
└── pyproject.toml      # Build system requirements
```

## Feature Development

When developing new features:

1. Configuration Files:
   - Add new options to default config in config.py
   - Document new options in README.md
   - Add validation in Config class

2. New Commands:
   - Add to cli.py
   - Include help text
   - Add tests in test_cli.py

3. Core Features:
   - Add to converter.py
   - Include type hints
   - Write comprehensive tests
   - Update documentation

## Documentation

- Keep README.md updated with new features
- Add docstrings to all new functions
- Include examples in docstrings
- Update CHANGELOG.md with changes

## Release Process

1. Update version:
   - __init__.py
   - CHANGELOG.md
   - setup.cfg (if needed)

2. Create release commit:
```bash
git add .
git commit -m "Release vX.Y.Z"
git tag vX.Y.Z
git push origin main --tags
```

3. Build and publish:
```bash
python -m build
python -m twine upload dist/*
```

## Getting Help

- Open an issue for bugs
- Use discussions for questions
- Tag issues appropriately

## Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team. All complaints will be reviewed and investigated promptly and fairly.

## License

By contributing to markdown2code, you agree that your contributions will be licensed under its Apache License.
