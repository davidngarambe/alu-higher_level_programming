#!/usr/bin/python3


def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Try to format and print as an integer
        return True  # Return True if successful
    except (ValueError, TypeError):  # Catch formatting errors
        return False  # Return False if not an integer
