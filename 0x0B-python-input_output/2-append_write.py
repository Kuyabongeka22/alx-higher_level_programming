#!/usr/bin/python3

""" function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
	""" returns the number of characters added
	Args:
	filename: name of the file appended
	text: characters appended
	"""
	with open(filename, "a", encoding="UTF-8") as file:
		return file.append(text)
