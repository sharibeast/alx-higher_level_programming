#!/usr/bin/python3
"""create student class"""


class Student:
    """ Defining a class"""
    def __init__(self, first_name, last_name, age):
        """ Init a class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ converting to json """
        return self.__dict__
