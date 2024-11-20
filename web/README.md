# markdown2code Web Interface

A web-based interface for the markdown2code tool, allowing you to convert markdown files to code through your browser.

## Features

- Direct markdown content input through text area
- File upload support for markdown files
- Automatic project.md file creation
- Real-time conversion feedback
- Error handling and display
- Clean, responsive UI

## Prerequisites

- Python 3.x
- pip (Python package installer)
- markdown2code package installed in development mode

## Installation

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

3. Use the web interface by either:
   - Entering markdown content directly in the text area
   - Uploading a markdown file

4. Click "Convert" to process your markdown and generate code files

## Project Structure

```
web/
├── app.py              # Flask application
├── requirements.txt    # Project dependencies
├── templates/         
│   └── index.html     # Web interface template
└── uploads/           # Directory for uploaded files
```

## Development

```
cd web && rm -rf venv && python -m venv venv && . venv/bin/activate && pip install -r requirements.txt && python app.py

python -m venv venv && . venv/bin/activate && pip install -r requirements.txt && python app.py

pip install --upgrade pip
 
open http://127.0.0.1:5000
 
python app.py
```
- The application uses Flask for the backend
- Frontend is built with vanilla HTML/CSS/JavaScript
- File uploads are handled securely
- Conversion results are returned as JSON

## Error Handling

The web interface handles various error cases:
- Invalid markdown content
- File upload issues
- Conversion failures
- Server errors

## Security Notes

- File size is limited to 16MB
- Only markdown files are accepted for upload
- Uploads directory is automatically created
- Files are processed in a secure manner
