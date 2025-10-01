"""Setup script for Exam Bank System"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="exambank-system",
    version="1.0.0",
    author="kornxi",
    description="A simple exam question bank management system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kornxi/exambank-system",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pytest>=7.4.0",
    ],
    entry_points={
        "console_scripts": [
            "exambank=app:main",
        ],
    },
)
