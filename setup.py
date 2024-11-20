from setuptools import setup, find_packages

setup(
    name="markdown2code",
    version="0.1.0",
    author="Tom Sapletta",
    author_email="info@softreck.dev",
    description="Convert markdown files to code files",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/plain-mark/markdown2code",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # Add dependencies here
    ],
    entry_points={
        'console_scripts': [
            'markdown2code=markdown2code.cli:main',
        ],
    },
)
