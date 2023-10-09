#!/usr/bin/python3
""" Returns sub clas """


def inherits_from(obj, a_class):
    """
    Return true when  object is an instance of a class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
