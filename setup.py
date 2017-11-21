from setuptools import setup
from setuptools import find_packages

setup(
    name='Docker-Spy',
    version='0.0.1',
    description='Output in Yaml networking info from your running containers',
    author='Nicolas Herbaut',
    author_email='nicolas.herbaut@univ-grenoble-alpes.fr',
    url='https://nextnet.top',
    scripts=['bin/docker-spy'],
    install_requires=
    ["certifi==2017.11.5",
     "chardet==3.0.4",
     "docker-py==1.10.6",
     "docker-pycreds==0.2.1",
     "idna==2.6",
     "netifaces==0.10.6",
     "PyYAML==3.12",
     "requests==2.18.4",
     "six==1.11.0",
     "urllib3==1.22",
     "websocket-client==0.44.0"],

    packages=find_packages()
)
