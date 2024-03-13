#!/usr/bin/python3

for first_digit in range(0, 10):
    for second_digit in range(1, 10):
        if first_digit > second_digit:
            continue
        else:
            print("{}, {}".format(first_digit, second_digit), end='')
