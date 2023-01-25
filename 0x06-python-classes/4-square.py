#!/usr/bin/python3
"""Square with size"""

class Square:
    """Representation of a square"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.size = size

    @property
    def size(self):
        """Property to retrieve size"""
        return (self.__size)
    @size.setter
    def size(self, value):
        """Property setter to set size"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        

    def area(self):
        """Public instance method that return the current area of the Square"""
        return (self.__size ** 2)
