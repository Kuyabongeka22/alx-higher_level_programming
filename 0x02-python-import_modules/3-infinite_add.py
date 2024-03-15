#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    no_of_arguments = len(argv) - 1
    '''removing the 1st argument from argv, which is the name of the file'''
    argv = argv[1::1]

    '''converting arguments to integers'''
    ints = []
    for argument in argv:
        ints.append(int(argument))

    results = sum(ints)
    print("{}".format(results))
