#!/usr/bin/python3

"""function that writes a string to a text file """


def write_file(filename="", text=""):
	""" returns the number of characters written in a text file
	Args:
	filename (str): The name of the file to write.
	text (str): The text to write to the file.
	Returns:
	The number of characters written.
	"""
	with open(filename, mode="w", encoding = "UTF8") as file:
		string = file.write(str())
		return len(string)
		
