from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="markdown2code",
    version="0.1.0",
    author="Plain Mark",
    author_email="",  # Add author email
    description="Convert markdown files into organized project structures with code files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/plain-mark/markdown2code",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'markdown2code=markdown2code.cli:main',
        ],
    },
    keywords="markdown, code generation, project structure, development tools",
    project_urls={
        "Bug Reports": "https://github.com/plain-mark/markdown2code/issues",
        "Source": "https://github.com/plain-mark/markdown2code",
    },
)
