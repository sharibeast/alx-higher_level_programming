#!/usr/bin/python3
"""
Returns True if the object exactly an instance of the speecified class
"""


def is_same_class(obj, a_class):
    """
    return true if obj is instance
    """

    return type(obj) is a_class
