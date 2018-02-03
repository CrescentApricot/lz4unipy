# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    li = f.read()

setup(
    name='lz4unipy',
    version='1.0.1',
    description='unity3d compatible lz4 pack/unpack library working on Python3.',
    long_description=readme,
    author='Cryptomelone',
    author_email='cryptomelone@users.noreply.github.com',
    license=li,
    url='https://github.com/Cryptomelone/lz4unipy',
    packages=find_packages(exclude=('tests',)),
    install_requires=["lz4"],
    entry_points={
        'console_scripts': [
            'lz4unipy = lz4unipy.cmd:main',
        ],
    }
)
