#!/usr/bin/python3
"""
Write obj to JSON file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write obj to JSON
    """
    with open(filename, "w", encoding="utf-8") as myfile:
        myfile.write(json.dumps(my_obj))
