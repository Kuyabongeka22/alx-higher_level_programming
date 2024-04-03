#!/usr/bin/python3

"""Define Square class"""


class Square:
    """Represents a square"""
    def __init__(self, __size=0):
        """initialises the __size"""
        try:
            self.__size = __size
        except:
            raise TypeError ("size must be an integer")
            raise ValueError ("size must be >= 0")
