# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('gana/gana.py').read(),
    re.M
    ).group(1)


setup(
    name = "cmdline-gana",
    packages = ["gana"],
    entry_points = {
        "console_scripts": ['gana = gana.gana:main']
        }
    )
