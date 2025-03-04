#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Convert lowercase letters to uppercase using ASCII values
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()  # Print a new line at this
