#!/usr/bin/python3
"""
A rectangle with width and height.
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Instantiation
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Setter for width
        """

        return self.__height

    @property
    def width(self, value):
        """ method that defines the width """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Setter for height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height
        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
