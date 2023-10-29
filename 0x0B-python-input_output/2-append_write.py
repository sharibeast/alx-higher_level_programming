#!/usr/bin/python3
"""Defines fn to append a file"""


def append_write(filename="", text=""):
    """Appending a string .
    Args:
        filename: Tname of the file to append to.
        text: The string to append to the file.
    Returns:
         number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
