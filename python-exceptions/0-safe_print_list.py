#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0  # Counter for printed elements
    try:
        for i in range(x):  # Attempt to print x elements
            print(my_list[i], end="")  # Print without newline
            count += 1  # Increment count if successful
    except IndexError:  # Catch if x is larger than list length
        pass
    print()  # Print newline after printing elements
    return count  # Return actual printed count
