# Contributing to markdown2code Web Interface

Thank you for your interest in contributing to the markdown2code web interface! This document provides guidelines and instructions for contributing to this part of the project.

## Development Setup

1. Fork and clone the repository:
```bash
git clone https://github.com/yourusername/markdown2code.git
cd markdown2code/web
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
python app.py
```

## Project Structure

```
web/
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
├── templates/         
│   └── index.html     # Web interface template
└── uploads/           # Upload directory (created automatically)
```

## Development Guidelines

### Flask Application (app.py)

- Keep the application modular and well-documented
- Use Flask best practices and patterns
- Handle errors gracefully with appropriate HTTP status codes
- Implement proper file handling and security measures
- Add logging for important operations
- Write docstrings for all functions

### Frontend (templates/index.html)

- Keep JavaScript code organized and commented
- Use semantic HTML elements
- Write maintainable CSS
- Ensure responsive design works correctly
- Implement proper error handling and user feedback
- Follow accessibility best practices

### Testing

When adding new features or making changes:

1. Test the web interface thoroughly:
   - File upload functionality
   - Direct markdown input
   - Error handling
   - Response handling
   - UI responsiveness

2. Test with various inputs:
   - Different markdown content
   - Various file sizes
   - Invalid inputs
   - Edge cases

### Pull Request Process

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes following the guidelines above

3. Test your changes thoroughly

4. Commit your changes with clear messages:
```bash
git commit -m "Add: brief description of your changes"
```

5. Push to your fork and create a pull request

6. Ensure your PR description clearly describes the changes

## Code Style

- Follow PEP 8 for Python code
- Use consistent indentation (4 spaces for Python)
- Write clear, descriptive variable and function names
- Add comments for complex logic
- Keep functions focused and modular

## Security Considerations

When contributing, ensure you:

- Validate all user inputs
- Handle file uploads securely
- Protect against common web vulnerabilities
- Don't expose sensitive information
- Follow secure coding practices

## Questions or Issues?

If you have questions or run into issues:

1. Check existing issues in the repository
2. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Any relevant error messages
