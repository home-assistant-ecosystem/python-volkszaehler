#!/usr/bin/env python3
"""Script to set up the Volkszaehler API wrapper."""
import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="volkszaehler",
    version="0.5.1",
    description="Python Wrapper for interacting with the Volkszahler API.",
    long_description=long_description,
    url="https://github.com/home-assistant-ecosystem/python-volkszaehler",
    download_url="https://github.com/home-assistant-ecosystem/python-volkszaehler/releases",
    author="Fabian Affolter",
    author_email="fabian@affolter-engineering.ch",
    license="MIT",
    install_requires=[
        "aiohttp>=3.8.4,<4",
        "async_timeout",
    ],
    packages=["volkszaehler"],
    python_requires=">=3.10",
    zip_safe=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
    ],
)
