import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SpiderChart_pkg",
    version="0.0.1",
    author="James Rabey",
    author_email="james.rabey@bulletproof.net",
    description="Generate a Spider (aka Radar) chart and email",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jrabeybpfac3/spiderchart.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
