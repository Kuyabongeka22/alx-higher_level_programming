#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv= sys.argv
    no_of_elements= len(argv) - 1

    if no_of_elements == 0:
        print("{} arguments.".format(no_of_elements))
    elif no_of_elements == 1:
        print("{} argument:".format(no_of_elements))
    else:
        print("{} arguments:".format(no_of_elements))

    for number in range(no_of_elements):
            print("{}: {}".format(number + 1, sys.argv[number + 1]))
