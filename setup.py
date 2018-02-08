# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

with open("requirements.txt") as requirements_file:
  install_requires = requirements_file.read().split("\n")

setup(
    name='Docker-Spy',
    version='0.0.6',
    description='Output in Yaml networking info from your running containers',
    author='Nicolas Herbaut',
    author_email='nicolas.herbaut@univ-grenoble-alpes.fr',
    url='https://nextnet.top',
    scripts=['bin/docker-spy'],
    install_requires=install_requires,
    packages=find_packages()
)
