#!/usr/bin/python3
"""Defination of a locked class"""


class LockedClass:
    """prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name"""
    
    __slots__ = {"first_name"}
