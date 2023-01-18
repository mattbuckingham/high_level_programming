#!/usr/bin/python3
for i in range(1, 99):
    if (i % 10) >= int(i / 10):
        print("{:02}, ".format(i), end="")
print("99")
