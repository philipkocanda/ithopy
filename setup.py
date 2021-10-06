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


from distutils.core import setup
setup(
  name = 'ithopy',
  packages = ['ithopy'],
  version = '0.1',
  license='MIT',
  description = 'IthoPy is a library to communicate with I2C Itho devices',   # Give a short description about your library
  author='Philip Kocanda',
  author_email='philip@kocanda.nl',
  url='https://github.com/philipkocanda/ithopy',
  download_url = 'https://github.com/philipkocanda/ithopy/archive/v_01.tar.gz',    # I explain this later on
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
