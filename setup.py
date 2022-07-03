from setuptools import setup

VERSION = "v1.0.0"

with open("README.md", "r") as f:
    desc = f.read()

setup(
    name="pyrostep",
    version=VERSION,
    description="A step handler library for pyrogram framework",
    long_description=desc, # COMPLETE THIS
    author="aWolver",
    url="https://github.com/aWolver/pyrostep",
    packages=["pyrostep"],
    requires=["pyrogram"],
)
