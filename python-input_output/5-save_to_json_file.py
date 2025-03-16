import json

def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file in JSON format.

    Args:
        my_obj (object): The Python object (e.g., list, dict) to be serialized.
        filename (str): The name of the file where the object will be saved.

    This function uses the json.dump() method to serialize the object
    and write it to the specified file. The file is opened in write mode
    ('w'), and the contents are saved in JSON format.

    The function automatically handles the opening and closing of the file
    using the `with` statement, ensuring that resources are managed properly.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
