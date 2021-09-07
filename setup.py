from setuptools import setup, find_packages

setup(
    name='pyga',
    version='0.1.0',
    url='https://github.com/jorahn/gapy-tools.git',
    author='Jonathan Rahn & Hoang Nguyen',
    author_email='jonathan.rahn@42digital.de',
    description='Google Analytics API Tools',
    packages=find_packages(),
    install_requires=['google-api-python-client >= 2.19.1', 'pandas >= 1.3.2'],
)
