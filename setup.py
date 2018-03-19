#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='psycopg2',    # This is the name of your PyPI-package.
    version='0.1',             # Update the version number for new releases
    packages=find_packages(),
    include_package_data=True
)
