#!/usr/bin/python3
""" My class (MyList) """


class MyList(list):
    """
    Inherit from class list
    """
    def print_sorted(self):
        """
        prints the list in sorted order
        """
        print(sorted(self))
