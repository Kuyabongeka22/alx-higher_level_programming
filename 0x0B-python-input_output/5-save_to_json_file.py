#!/usr/bin/python3

"""function that writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
	"""write using JSON"""
	json_obj = json.dumps(my_obj)
	with open(filename, "w") as jsonFile:
		jsonFile.write(json_obj)
