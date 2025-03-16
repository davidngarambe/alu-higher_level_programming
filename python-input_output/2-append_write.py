#!/usr/bin/python3
"""
Module for appending a string to a UTF-8 text file.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
