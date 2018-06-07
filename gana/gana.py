# -*- coding: utf-8 -*-

__version__ = "0.2.0"


import sys
import yaml
from subprocess import call

def main():
    print("""    __
    __----__
    {   p p  }
    {____||__}__
    /  || \/ /
    / /  - |_/
    \_\    |
    |= = =|
    '-----'
    |_) |_)""")
    with open('./gana/definition.yml', 'r') as stream:
        try:
            definition = yaml.load(stream)
            with open('data.yml', 'w') as outfile:
                yaml.dump(definition['build'],outfile,default_flow_style=False)
        except yaml.YAMLError as exc:
            print(exc)
    status = call("jenkins-jobs --conf ./jenkins/jenkins.ini update data.yml")