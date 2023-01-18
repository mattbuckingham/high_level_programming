#!/usr/bin/python3
char = 97
for i in range(26):
    if chr(char+i) not in ['e', 'q']:
        print("{}".format(chr(char + i)), end="")
