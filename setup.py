# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import zambiaureport
version = zambiaureport.__version__

setup(
    name='zambiaureport',
    version=version,
    author='',
    author_email='andre@andrelesa.com',
    packages=[
        'zambiaureport',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['zambiaureport/manage.py'],
)