from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements=f.read().splitlines()

setup(
    name="Titanic_ETL",
    version="0.1",
    author="Allen Tider",
    packages=find_packages(),
    install_requires = requirements,
)