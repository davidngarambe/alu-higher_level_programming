#!/usr/bin/python3
"""
Module for converting a JSON string to a Python object.
"""

import json


def from_json_string(my_str):
    """Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python data structure.
    """
    return json.loads(my_str)
