# setup.py

from setuptools import setup, find_packages

setup(
    name="dexter-encoder",             # Unique package name
    version="1.0.0",                   # Initial version
    author="Ethan Fraser",             # Your name
    author_email="ethanprime.c137@mail.com",  # Your email
    description="A custom encoding library for shellcode obfuscation.",
    long_description=open("README.md").read(),  # Description from README.md
    long_description_content_type="text/markdown",
    url="https://github.com/Brownpanda29/dexter",  # GitHub project URL
    packages=find_packages(),          # Finds and includes all modules in the package
    classifiers=[                      # Optional package metadata
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',           # Minimum Python version
)
