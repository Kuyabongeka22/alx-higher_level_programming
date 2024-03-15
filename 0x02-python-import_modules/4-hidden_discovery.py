#!/usr/bin/python3

if __name__ == "__main__":
    import importlib.util

    file_path = 'C:/Users/student/Downloads'

    x = dir(file_path)

    if not x == "__ ...":
        print("{}".format(x))
