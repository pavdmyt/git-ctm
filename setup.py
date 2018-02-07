#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs

from setuptools import setup

try:
    # Python 3
    from os import dirname
except ImportError:
    # Python 2
    from os.path import dirname


here = os.path.abspath(dirname(__file__))


with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


required = [
    'docopt',
]

setup(
    name='git-ctm',
    version='0.1.0',
    description='Git commit time machine.',
    long_description=long_description,
    author='Pavlo Dmytrenko',
    author_email='mail@pavdmyt.com',
    url='https://github.com/pavdmyt/git-ctm',
    py_modules=['ctm'],
    install_requires=required,
    license='MIT',
    entry_points={
        'console_scripts': [
            'ctm = ctm:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)