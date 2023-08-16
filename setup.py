"""Setup."""

from setuptools import setup

setup(
    name="Dummy",
    author="MenSeb",
    version="1",
    package_data={"dummy": ["py.typed"]},
    packages=["dummy"],
)
