#!/usr/bin/python3

"""function that returns the JSON representation of an object"""


def to_json_string(my_obj):
	"""returns JSON format"""
	return json.dump(my_obj)
