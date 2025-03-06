#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []  # List to store division results
    for i in range(list_length):
        try:
            # Check if both elements exist in the lists
            num1 = my_list_1[i]
            num2 = my_list_2[i]

            # Perform division if both elements are numbers
            result = num1 / num2
        except IndexError:
            print("out of range")  # List index out of range
            result = 0
        except ZeroDivisionError:
            print("division by 0")  # Division by zero
            result = 0
        except TypeError:
            print("wrong type")  # Non-numeric type
            result = 0
        finally:
            new_list.append(result)  # Append result (or 0 if an exception occurred)

    return new_list  # Return the new list with division results
