"""
Core functionality for converting markdown to code files
"""
import os
import re
from pathlib import Path

DEFAULT_FILENAMES = {
    'javascript': 'script.js',
    'js': 'script.js',
    'python': 'script.py',
    'py': 'script.py',
    'css': 'styles.css',
    'html': 'index.html',
    'java': 'Main.java',
    'cpp': 'main.cpp',
    'c': 'main.c',
    'sql': 'query.sql',
    'php': 'index.php',
    'ruby': 'script.rb',
    'go': 'main.go',
    'rust': 'main.rs',
    'typescript': 'script.ts',
    'ts': 'script.ts',
    'yaml': 'config.yml',
    'yml': 'config.yml',
    'json': 'config.json',
    'xml': 'config.xml',
    'markdown': 'README.md',
    'md': 'README.md',
    'bash': 'script.sh',
    'sh': 'script.sh',
    'dockerfile': 'Dockerfile'
}

class MarkdownConverter:
    def __init__(self, input_file, output_dir='.'):
        self.input_file = input_file
        self.output_dir = output_dir

    @staticmethod
    def extract_filename_from_comments(content):
        """Extract filename from various comment types."""
        patterns = [
            r'(?:^|\n)//\s*([^\n]*\.[\w]+)',  # JavaScript, C++
            r'(?:^|\n)#\s*([^\n]*\.[\w]+)',   # Python, Bash, Ruby
            r'/\*\s*(.*?\.[\w]+).*?\*/',       # C-style (/* */)
            r'<!--\s*(.*?\.[\w]+).*?-->',      # HTML/XML
            r'"""\s*(.*?\.[\w]+).*?"""',       # Python docstring
            r"'''\s*(.*?\.[\w]+).*?'''",       # Python docstring (single quotes)
            r'--\s*([^\n]*\.[\w]+)',          # SQL
            r'%\s*([^\n]*\.[\w]+)',           # LaTeX
        ]

        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL)
            if match:
                filename = match.group(1).strip()
                if '.' in filename:
                    return filename

        return None

    def extract_file_content(self, markdown_content):
        """Extract file content from markdown code blocks."""
        pattern = r'```(\w+)?\s*(?:#\s*(.*?)\n|\n)?(.*?)```'
        matches = re.finditer(pattern, markdown_content, re.DOTALL)

        files_content = {}
        file_counter = {}

        for match in matches:
            language = match.group(1)
            comment = match.group(2)
            content = match.group(3).strip()

            if language == 'markdown' and 'media-monitor/' in content:
                continue

            filename = None

            if comment and ('.' in comment or '/' in comment):
                filename = comment.strip()

            if not filename:
                filename = self.extract_filename_from_comments(content)

            if not filename and language:
                language = language.lower()
                if language in DEFAULT_FILENAMES:
                    base_name = DEFAULT_FILENAMES[language]
                    if base_name in file_counter:
                        file_counter[base_name] += 1
                        name, ext = os.path.splitext(base_name)
                        filename = f"{name}_{file_counter[base_name]}{ext}"
                    else:
                        file_counter[base_name] = 0
                        filename = base_name

            if filename:
                files_content[filename] = content

        return files_content

    @staticmethod
    def create_directory_structure(structure_text):
        """Create a list of paths from text directory structure."""
        paths = []
        for line in structure_text.split('\n'):
            line = line.strip()
            if not line or '```' in line:
                continue

            path = re.sub(r'^[│├└─\s]+', '', line)
            if path and not path.startswith('#'):
                if not ('.' in path) and not path.endswith('/'):
                    path += '/'
                paths.append(path)

        return paths

    @staticmethod
    def ensure_directory(file_path):
        """Create directories for the given file path."""
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def preview(self):
        """Preview what files will be generated without creating them."""
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                content = f.read()

            output_path = Path(self.output_dir)
            preview_info = {
                'directories': [],
                'files': [],
                'conflicts': []
            }

            # Check directory structure
            structure_match = re.search(r'```markdown\n(.*?)\n```', content, re.DOTALL)
            if structure_match:
                paths = self.create_directory_structure(structure_match.group(1))
                for path in paths:
                    full_path = output_path / path
                    if path.endswith('/'):
                        preview_info['directories'].append({
                            'path': str(full_path),
                            'exists': full_path.exists()
                        })

            # Check files
            files_content = self.extract_file_content(content)
            for filename, _ in files_content.items():
                clean_filename = filename.replace('# ', '').strip()
                file_path = output_path / clean_filename
                preview_info['files'].append({
                    'path': str(file_path),
                    'exists': file_path.exists()
                })
                if file_path.exists():
                    preview_info['conflicts'].append(str(file_path))

            return preview_info

        except Exception as e:
            print(f"An error occurred during preview: {str(e)}")
            raise

    def convert(self, force=False):
        """Convert markdown file to code files."""
        preview_info = self.preview()
        
        # Print preview information
        print("\nFiles to be created:")
        for dir_info in preview_info['directories']:
            status = "exists" if dir_info['exists'] else "will be created"
            print(f"Directory: {dir_info['path']} ({status})")
        
        for file_info in preview_info['files']:
            status = "exists" if file_info['exists'] else "will be created"
            print(f"File: {file_info['path']} ({status})")
        
        if preview_info['conflicts'] and not force:
            print("\nWarning: The following files already exist:")
            for conflict in preview_info['conflicts']:
                print(f"- {conflict}")
            raise FileExistsError(
                "Some files already exist. Use --force to overwrite or choose a different output directory."
            )

        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                content = f.read()

            output_path = Path(self.output_dir)
            output_path.mkdir(parents=True, exist_ok=True)

            structure_match = re.search(r'```markdown\n(.*?)\n```', content, re.DOTALL)
            if structure_match:
                paths = self.create_directory_structure(structure_match.group(1))
                for path in paths:
                    full_path = output_path / path
                    if path.endswith('/'):
                        full_path.mkdir(parents=True, exist_ok=True)
                    else:
                        self.ensure_directory(str(full_path))

            files_content = self.extract_file_content(content)
            created_files = []

            for filename, file_content in files_content.items():
                clean_filename = filename.replace('# ', '').strip()
                file_path = output_path / clean_filename
                self.ensure_directory(str(file_path))

                print(f"Creating file: {file_path}")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(file_content + '\n')

                if clean_filename.endswith('.sh'):
                    os.chmod(file_path, 0o755)

                created_files.append(clean_filename)

            print("\nCreated files:")
            for f in sorted(created_files):
                print(f"- {f}")
            print("\nProject structure created successfully!")

            return created_files

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise
