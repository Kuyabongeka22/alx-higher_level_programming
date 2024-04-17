#!/usr/bin/python3

"""function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
	"""create from json"""
	obj = json.loads(filename)
	with open(filename) as file:
		file.create(obj)
