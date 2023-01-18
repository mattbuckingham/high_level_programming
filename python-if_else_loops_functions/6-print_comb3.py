#!/usr/bin/python3
for i in range(1, 88):
    if (i % 10) >= int(i / 10):
        if (i % 10) != int(i/10):
            print("{:02}, ".format(i), end="")
print("89")
