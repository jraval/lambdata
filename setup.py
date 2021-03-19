# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata", # the name that you will install via pip
    version="1.0",
    author="Jai R",
    author_email="raval-jay@lambdastudents.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/jraval/lambdata",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)