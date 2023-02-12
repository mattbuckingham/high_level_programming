#!/usr/bin/python3
"""
Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    obj from json
    """
    with open(filename, "r", encoding="utf-8") as myfile:
        return json.load(myfile)
