#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup


try:
    # Python 3
    from os import dirname
except ImportError:
    # Python 2
    from os.path import dirname


here = os.path.abspath(dirname(__file__))


def read_version(module_name):
    with open(module_name, 'r') as fd:
        for line in fd:
            if line.startswith('__version__ = '):
                return line.split()[-1].strip().strip("'")


with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


required = [
    'docopt',
]


setup(
    name='git-ctm',
    version=read_version('ctm.py'),
    author='Pavlo Dmytrenko',
    author_email='mail@pavdmyt.com',
    license='MIT',
    description='Git commit time machine.',
    long_description=long_description,
    url='https://github.com/pavdmyt/git-ctm',
    download_url='https://github.com/pavdmyt/git-ctm/archive/master.zip',
    py_modules=['ctm'],
    install_requires=required,
    entry_points={
        'console_scripts': [
            'ctm = ctm:main',
        ]
    },
    platforms=['any'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Software Development :: Version Control',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Utilities',
    ]
)
