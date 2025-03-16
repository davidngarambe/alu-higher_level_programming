#!/usr/bin/python3
"""
Module for writing a string to a UTF-8 text file.
"""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write into the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
