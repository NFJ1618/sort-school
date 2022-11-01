import os
from setuptools import setup, find_packages


with open("requirements.txt", "r") as f:
    reqs = [line.rstrip("\n") for line in f if line != "\n"]


setup(
    name='Page Shuffler',
    packages=find_packages(),
    install_requires=reqs,
    #url='https://github.com/NFJ1618/page-shuffler',
    license='MIT',
    author='Jai Parera',
    author_email='jaiparera@g.ucla.edu',
    description='A simple web-app based to upload, shuffle, and download your PDF files'
    )