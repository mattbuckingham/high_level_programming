#!/usr/bin/python3
"""
prints text and inserts newlines
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of these characters: ., ? and :
    """

    text = text.strip()
    previous_char = None
    for char in text:
        if char in ["?", ":", "."]:
            print(f"{char} \n")
            previous_char = "\n"
        elif char == " " and previous_char == "\n":
            pass
        else:
            print(char, end="")
            previous_char = char
