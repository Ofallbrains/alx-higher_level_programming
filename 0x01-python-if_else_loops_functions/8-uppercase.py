#!/usr/bin/python3
def uppercase(str):
    for j in str:
        if ord(j) > 96 and ord(j) < 123:
            j = chr(ord(j) - 32)
        print("{}".format(j), end="")
    print("")
