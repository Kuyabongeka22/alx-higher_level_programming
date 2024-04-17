#!/usr/bin/python3

"""Defines a text file-reading function."""


def read_file(filename=""):
	"""Defines a text file-reading function."""
	with open(filename, "r", encoding = "UTF8") as file:
		print(file.read(), end="")
