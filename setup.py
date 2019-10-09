from setuptools import find_packages
from setuptools import setup

NAME = 'ccvs-api-client'
VERSION = '0.0.1.dev4'

REQUIRES = [
    'requests==2.20.0',
    'Click==7.0',
    'six==1.12.0',
]

setup(
    name=NAME,
    version=VERSION,
    description='CCVS API Client',
    author_email='',
    url='',
    keywords=['CCVS API'],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
        Client for Central Container Vulnerability Scanning API
    """
)
