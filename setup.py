import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stats_pkg",
    version="0.0.1",
    author="Giannopoulos Giannis",
    author_email="gianisgianno@gmail.com",
    description="Stats calculation from a request",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/igianop/Stats-with-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
