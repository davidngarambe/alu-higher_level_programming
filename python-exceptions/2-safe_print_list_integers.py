#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0  # To count the number of printed integers
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")  # Print integer in formatted way
            count += 1  # Increment count if successfully printed
        except (ValueError, TypeError):
            continue  # Skip non-integer values silently
        except IndexError:
            break  # Stop if x exceeds the list length
    print()  # Print a newline at the end
    return count  # Return the count of printed integers
