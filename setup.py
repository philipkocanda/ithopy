# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
  name = 'ithopy',
  packages = ['ithopy'],
  version = '0.1',
  license='MIT',
  description = 'IthoPy is a library to communicate with I2C Itho devices',   # Give a short description about your library
  long_description=readme,
  long_description_content_type='text/markdown',
  author='Philip Kocanda',
  author_email='philip@kocanda.nl',
  url='https://github.com/philipkocanda/ithopy',
  download_url = 'https://github.com/philipkocanda/ithopy/archive/refs/tags/v0.1.zip',    # I explain this later on
  keywords = ['itho', 'i2c'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
