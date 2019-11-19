from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dspy",
    version="0.0.1",
    author="xa4ypiva",
    author_email="khmelnitskii.vladislav@gmail.com",
    description="DSP routines written in Python",
    long_description=long_description,
    url="github.com/Xa4yPiva/dspy",
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                 "Operating System :: OS Independent"],
    install_requires=['numpy']
)
