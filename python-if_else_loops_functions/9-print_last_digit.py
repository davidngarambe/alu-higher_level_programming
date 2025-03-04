#!/usr/bin/python3


def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the last digit (handle negatives)
    print(last_digit, end="")  # Print without newline
    return last_digit  # Return the last digit
