#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""


class MyList(list):
    """inside a sub-class"""

    pass

    def print_sorted(self):
        """method to sort list"""
        print(sorted(list(self)))
