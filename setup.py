from setuptools import setup

with open("README.md") as f:
    long_description = f.read()
    
setup(
    name = "Trackarma",
    version = "1.0",
    description = "A python script that tracks reddit karma",
    license = "MIT",
    long_description = long_description,
    author = "Param Thakkar",
    author_email = "contact@param.me",
    url = "https://github.com/paramt/trackarma",
    packages = find_packages(exclude=("test")),
    install_requires = ["matplotlib", "praw"]
)
