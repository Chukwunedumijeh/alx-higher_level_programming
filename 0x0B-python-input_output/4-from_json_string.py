#!/usr/bin/python3
"""function that returns an object epresented by a JSON string
"""
import json


def from_json_string(my_str):
    """Returns a python object represented by a JSON string
    """

     return json.loads(my_str)
