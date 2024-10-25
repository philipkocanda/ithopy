# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='ithopy',
    packages=find_packages(exclude=('tests', 'tests.*')),
    version='0.2.3',
    license='MIT',
    description='IthoPy is a library to communicate with I2C Itho devices',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Philip Kocanda',
    author_email='philip@kocanda.nl',
    url='https://github.com/philipkocanda/ithopy',
    download_url='https://github.com/philipkocanda/ithopy/archive/refs/tags/v0.2.3.zip',
    keywords=['itho', 'i2c'],
    install_requires=[],
    python_requires='>=3.11',
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
