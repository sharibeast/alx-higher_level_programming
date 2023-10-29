#!/usr/bin/python3
"""definition  file-writing function."""


def write_file(filename="", text=""):
    """Write string to a UTF"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
