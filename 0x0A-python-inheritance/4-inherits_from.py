#!/usr/bin/python3
"""
function that returns True if the object is an instance 0f a class
"""


def inherits_from(obj, a_class):
    """function that inherits the class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
