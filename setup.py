import os
from setuptools import setup, find_packages


with open("requirements.txt", "r") as f:
    reqs = [line.rstrip("\n") for line in f if line != "\n"]


setup(
    name='Sort School',
    packages=find_packages(),
    install_requires=reqs,
    url='https://github.com/NFJ1618/sort-school',
    license='MIT',
    author='Jai Parera',
    author_email='jaiparera@g.ucla.edu',
    description='A simple web-app to visually teach you about sorting algorithms!'
    )