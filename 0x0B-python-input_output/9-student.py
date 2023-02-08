#!/usr/bin/python3
"""Student Class
"""


class student:
    """contains the student data
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary of Student
        """
        return self.__dict__
