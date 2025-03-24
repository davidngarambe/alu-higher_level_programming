#!/usr/bin/python3

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The object to serialize and write to the file.
        filename: The name of the file to write to.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
