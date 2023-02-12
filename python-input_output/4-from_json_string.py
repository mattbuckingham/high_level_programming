#!/usr/bin/python3
"""
Generate python obj from JSON
"""
import json


def from_json_string(my_str):
    """
    JSON to obj
    """
    return json.loads(my_str)
