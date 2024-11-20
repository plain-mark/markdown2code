"""
Command-line interface for markdown2code
"""
import argparse
import sys
from . import __version__

def main():
    parser = argparse.ArgumentParser(
        description="Convert markdown files to code files"
    )
    parser.add_argument(
        '--version',
        action='version',
        version=f'markdown2code {__version__}'
    )
    parser.add_argument(
        'input',
        help='Input markdown file'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output directory (default: current directory)',
        default='.'
    )

    args = parser.parse_args()
    
    # TODO: Implement conversion logic
    print(f"Processing {args.input} -> {args.output}")

if __name__ == '__main__':
    sys.exit(main())
