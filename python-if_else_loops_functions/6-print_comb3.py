#!/usr/bin/python3
for i in range(1, 99):
    if (i % 10) >= int(i / 10):
        print("{:02}, ".format(i), end="")
print("99")



""""
i = 1
while i <= 99:
    print("{:02}, ".format(i), end="")
    if (i % 10) % 9 == 0:
        i = i + int(i / 10)
    else:
        i = i + 1
print("99")
"""
