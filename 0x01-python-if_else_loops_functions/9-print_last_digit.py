#!/usr/bin/python3

def print_last_digit(number):
    results = abs(number) % 10
    print("{}".format(results), end='')
    return results
