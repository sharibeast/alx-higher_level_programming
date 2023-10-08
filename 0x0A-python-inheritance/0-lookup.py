#!/usr/bin/python3
""" create a function """


def lookup(obj):
    """
    Returns the list of available attributes & methods of obj
    """
    return dir(obj)
