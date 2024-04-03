#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    for elements in range (x):
        try:
            print("{:d}".format(my_list[elements]))
        except (ValueError, IndexError):
            pass
        else:
            return my_list[elements]
