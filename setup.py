from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME-RECOMMENDER-SYSTEM",
    version="1",
    author="Huzaifa Mahmood",
    packages=find_packages(),
    install_requires = requirements,
)