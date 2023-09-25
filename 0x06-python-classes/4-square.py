#!/usr/bin/python3
class Square:
    """class Square"""

    def __init__(self, size=0):
        """method to initialize"""
        self.size = size

    @property
    def size(self):
        """ Getter method to retrieve """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Setter method to initialize the size value """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ method to return current square area """
        return (self.__size**2)
