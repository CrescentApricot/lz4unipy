# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()
with open('LICENSE') as f:
    li = f.read()

setup(
    name='lz4unipy',
    version='2.0.1',
    description='unity3d compatible lz4 (un)compress tool working on Python3.',
    long_description=long_description,
    author='CrescentApricot',
    author_email='anzu-noreply@googlegroups.com',
    license=li,
    url='https://github.com/CrescentApricot/lz4unipy',
    packages=find_packages(exclude=('tests',)),
    install_requires=["lz4 < 3.0.0"],
    entry_points={
        'console_scripts': [
            'lz4unipy = lz4unipy.cmd:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Archiving :: Compression",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
