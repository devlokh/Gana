# -*- coding: utf-8 -*-

__version__ = "0.2.0"


import sys
import yaml

def main():
    with open("./gana/definition.yml", 'r') as stream:
        try:
            print(yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc['job'])