#!/usr/bin/python3
"""read file
"""


def read_file(filename=""):
    """function that read from a file
    """

    with open(filename, 'r', encoding="utf-8") as readFile:
        print(readFile.read(), end="")
