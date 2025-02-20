#!/usr/bin/python3
for i in range(0, 9):  # Outer loop for the first digit
    for j in range(i + 1, 10):  # Inner loop for the second digit
        if i == 8 and j == 9:  # If it's the last pair, print without a comma
            print(f"{i}{j}")
        else:
            print(f"{i}{j}", end=", ")
