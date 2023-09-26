#!/usr/bin/python3
""" Creating a class square """


class Square:
    """ the Class constructor definition """
    def __init__(self, size=0):
        """Initialize instance square class
        Args: size=0: size of square
        """
        self.__size = size

    @property
    def size(self):
        """ sett getter of the square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting the size of the square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getting position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive intergers")
        if not isinstance(valu[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive intergers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive intergers")
        self.__position = value

    def area(self):
        """ Calculate the area of the sqaure """
        return self.__size ** 2

    def my_print(self):
        """ Print the sq """
        if self.__size == 0:
            print()
            return
        [print("") for x in range(0, self.__position[1])]
        for n in range(0, self.__size):
            [print(" ", end="")for q in range(0, self.__position[0])]
            [print("#", end="")for y in range(0, self.__position[0])]
            print()
