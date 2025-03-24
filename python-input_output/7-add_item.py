#!/usr/bin/python3

"""
Script that adds all command-line arguments to a list
and saves them in a JSON file.
"""

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Try loading existing data, if the file doesn't exist, start with an empty list
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add new arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
