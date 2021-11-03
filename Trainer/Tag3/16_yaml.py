#!/usr/bin/env python3
import yaml
import json

file = "/home/coder/aktueller-kurs/materialien/config.yaml"

data_loaded = yaml.safe_load(open(file))

print(type(data_loaded))
for k, v in data_loaded.items():
    print(k, v)

with open("converted.json", "w") as fd:
    fd.write(json.dumps(data_loaded))

def copy_yaml2json(yaml_file, json_file):
    with open(json_file, "w") as fd:
        fd.write(yaml.safe_load(open(yaml_file)))