#!/usr/bin/python3
"""  a function that adds new attributes to object """


def add_attribute(obj, name, value):
    """ add_attribute function """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)