#!/usr/bin/python3

import json

"""
    Serializes a Python object and writes it to a file in JSON format.

    Args:
        my_obj (object): The Python object to be serialized (e.g., list, dict, etc.).
        filename (str): The name of the file where the JSON representation of `my_obj` will be saved.

    The function uses the `json.dump()` method from the `json` module to serialize the object and write it 
    to the specified file. The file is opened in write mode ('w'), and the content is saved as JSON.
    
    The `json.dump()` function converts the Python object into JSON format. The function handles opening and 
    closing the file using the `with` statement, ensuring that the file is closed properly after the write operation.
    """

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        # json.dump() serializes the Python object into JSON format and writes it to the file
        json.dump(my_obj, file)
