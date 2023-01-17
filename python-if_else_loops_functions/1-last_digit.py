#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if digit > 5:
    string = "and is greater than 5"
elif digit == 0:
    string = "and is 0"
else:
    string = "and is less than 6 and not 0"
print(f"Last digit of {number} is {digit} {string}")
