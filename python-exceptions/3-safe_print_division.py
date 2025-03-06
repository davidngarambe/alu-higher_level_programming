#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        result = a / b  # Perform division
    except ZeroDivisionError:
        result = None  # Handle division by zero
    finally:
        print("Inside result: {}".format(result))  # Always print the result
    return result  # Return the division result (or None if division by zero)
