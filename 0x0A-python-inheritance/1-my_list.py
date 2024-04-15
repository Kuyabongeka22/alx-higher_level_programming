#!/usr/bin/python3
"""creates a class that inheritates"""


class MyList(list):
    """inside a sub-class"""

    pass

    def print_sorted(self):
        """method to sort list"""
        print(sorted(list(self)))
