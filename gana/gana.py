# -*- coding: utf-8 -*-

__version__ = "0.2.0"


import sys
import yaml

def main():
    with open('./gana/definition.yml', 'r') as stream:
        try:
            definition = yaml.load(stream)
            with open('data.yml', 'w') as outfile:
                yaml.dump(definition['build'],outfile,default_flow_style=False)
        except yaml.YAMLError as exc:
            print(exc)

main()