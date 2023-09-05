#!/usr/bin/python3
def uppercase(str):
    for w in str:
        if (ord(w) > 96 and ord(w) <= 124):
            w = chr(ord(w) - 32)
        print("{}".format(w), end="")
    print()
