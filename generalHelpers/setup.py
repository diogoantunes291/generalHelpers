from setuptools import setup, find_packages

setup(
    name="generalHelpers",
    version="0.1",
    packages=find_packages(include=["generalHelpers", "generalHelpers.*"]),
    include_package_data=True
)