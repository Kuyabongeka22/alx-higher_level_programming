#!/usr/bin/python3

def write_file(filename="", text=""):
	with open(filename, mode="w", encoding = "UTF8") as file:
		string = file.write(str())
		return len(string)
		
