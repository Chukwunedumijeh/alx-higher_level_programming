#!/usr/bin/python3
"""write file
"""


def write_file(filename="", text=""):
    """Take str file name to read and str text to write to
    """

    with open(filename, 'w', encoding="utf-8") as writeFile:
        return writeFile.write(text)
