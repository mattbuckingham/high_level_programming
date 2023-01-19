#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            upper = chr(ord(i) - 32)
        else:
            upper = i;
        print("{}".format(upper), end = "")
    print()
