#!/usr/bin/python3

def uppercase(str):
    for letters in str:
        if ord(letters) > 96 and ord(letters) < 123:
            letters = chr(ord(letters) - 32)
        print("{}".format(str))
