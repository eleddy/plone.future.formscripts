# -*- coding: utf-8 -*-
"""Installer for the plone.future.formscripts package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='plone.future.formscripts',
    version='0.1',
    description="Migration away from cpt/cpy/vpy to browser views. Plone 5 preview",
    long_description=long_description,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='plone',
    author='Elizabeth Leddy',
    author_email='eleddy@plone.org',
    url='http://pypi.python.org/pypi/plone.future.formscripts',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['plone.future'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Plone',
        'setuptools',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
