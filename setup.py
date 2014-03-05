#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


setup(name='time-after-time',
      version='0.0.1',
      description='A tiny library to parse out various time grammars',
      author='Ryan Kanno',
      author_email='ryankanno@localkinegrinds.com',
      packages=find_packages('time_after_time', exclude=['tests']),
      long_description=open('README.md').read(),
      url="https://github.com/ryankanno/time-after-time")

# vim: filetype=python
