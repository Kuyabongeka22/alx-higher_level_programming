#!/usr/bin/python3

"""function that writes a string to a text file """


def write_file(filename="", text=""):
	""" returns the number of characters written in a text file"""
	with open(filename, mode="w", encoding = "UTF8") as file:
		string = file.write(str())
		return len(string)
		
