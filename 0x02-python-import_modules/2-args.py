#!/usr/bin/python3
import sys

argv= sys.argv
no_of_elements= len(argv) - 1

if no_of_elements == 0:
    print("{} arguments.".format(no_of_elements))
elif no_of_elements == 1:
    print("{} argument:".format(no_of_elements))
else:
    print("{} arguments:".format(no_of_elements))

total_arguments= len(argv)
for i in range(1, total_arguments):
    for number in range(1, total_arguments):
        print("{}: {}".format(number, sys.argv[i]))
