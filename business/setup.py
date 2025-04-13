#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='business',
    version='0.0.1',
    description='Custom Library for JobScraper',
    author='',
    author_email='',
    packages=find_packages(exclude=['tests.*', 'tests']),
    python_requires='>=3.8.*',
    include_package_data=True
)
