#!/usr/bin/env python
# -*- coding:utf8 -*-
"""Set up script."""
from setuptools import setup, find_packages
import os
import codecs
import re


HERE = os.path.dirname(os.path.abspath(__file__))


def _fetch_readme(filename):
    readme_path = os.path.join(HERE, filename)
    try:
        with codecs.open(readme_path, encoding='utf8') as f:
            readme = f.read()
    except IOError:
        readme = ''
    return readme


def _fetch_package_version(filename):
    source_path = os.path.join(HERE, filename)
    try:
        with codecs.open(source_path, encoding='utf8') as f:
            version_source = f.read()
        version_match = re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]", version_source, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")
    except IOError:
        raise RuntimeError('Source is not found.')


setup(
    name="idcfcloud-dns",
    version=_fetch_package_version('src/idcfcloud_dns.py'),
    url='https://github.com/attakei/idcfcloud-dns',
    author='attakei',
    author_email='attakei@gmail.com',
    description='IDCF cloud DNS client',
    long_description=_fetch_readme('README.rst'),
    packages=find_packages(),
    package_dir={'': 'src'},
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
    ],
)
