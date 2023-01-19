#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    digit = number - (10 * int(number / 10))
    print(f"{digit}", end="")
    return digit
