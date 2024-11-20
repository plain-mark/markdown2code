import logging
from markdown2code.converter import MarkdownConverter

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create converter instance
converter = MarkdownConverter("test_boundaries.txt", "test_output")

# Read the input file
with open("test_boundaries.txt", "r") as f:
    content = f.read()

# Extract files
files = converter.extract_file_content(content)

# Print debug info
print("\nFound files:")
for filename, content in files.items():
    print(f"\n{filename}:")
    print("-" * 40)
    print(content)
    print("-" * 40)
