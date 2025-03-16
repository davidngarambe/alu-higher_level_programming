#!/usr/bin/python3
"""
Module for reading a UTF-8 text file and printing its content.
"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
