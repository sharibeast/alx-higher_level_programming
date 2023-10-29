#!/usr/bin/python3
"""Define  string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Returns JSON  of a string object."""
    return json.dumps(my_obj)
