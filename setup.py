# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ithopy',
    version='0.1.0',
    description='IthoPy is a library to communicate with I2C Itho devices',
    long_description=readme,
    author='Philip Kocanda',
    author_email='philip@kocanda.nl',
    url='https://github.com/philipkocanda/ithopy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
