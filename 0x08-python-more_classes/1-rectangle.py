#!/usr/bin/python3
"""Defination of rectangle class"""


class Rectangle:
    """
    class rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        if not isinstance(width, int):
            raise TypeError(
                "width must be an integer"
            )
        if width < 0:
            raise ValueError("width must be >= 0")
        self.height = height
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def width(self):
        return self.width
    def width(self, value):
        self.width = value
    def height(self):
        return self.height
    def height(self, value):
        self.height = value

