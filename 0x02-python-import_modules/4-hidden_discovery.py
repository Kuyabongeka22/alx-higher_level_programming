#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import hidden_4

    x = dir(hidden_4)
    for name in x:
        if not name[1:] == "__":
            print("{}".format(name))
