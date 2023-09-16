#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    items = a_dictionary.items()
    for i, j in sorted(items):
        print("{}: {}".format(i, j))
