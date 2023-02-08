#!/usr/bin/python3
"""load_from_json_file
"""
import json


def load_from_json_file(filename):
    """Returns an object created from a json file
    """

    with open(filename, mode="r", encoding="UTF-8") as readFile:
        return json.load(readFile) 
