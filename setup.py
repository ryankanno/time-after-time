#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import time_after_time

packages = [
    'time_after_time'
]

requires = ['pyparsing', 'python-dateutil', 'py-utilities==0.0.2']
tests_require = ['flake8', 'mock', 'nose', 'nosexcover']

with open('README.rst') as f:
    readme = f.read()

with open('CHANGES') as f:
    changes = f.read()

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'License :: OSI Approved :: MIT License',
    'Topic :: Utilities'
]

setup(
    name='time-after-time',
    version=time_after_time.__version__,
    description='A tiny library to parse out various time grammars',
    long_description=readme + '\n\n' + changes,
    author='Ryan Kanno',
    author_email='ryankanno@localkinegrinds.com',
    url="https://github.com/ryankanno/time-after-time",
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'time_after_time': 'time_after_time'},
    install_requires=requires,
    license='MIT',
    tests_require=tests_require,
    classifiers=classifiers,
)

# vim: filetype=python
