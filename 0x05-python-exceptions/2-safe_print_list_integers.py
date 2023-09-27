#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    m = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            m = m + 1
            for y in range(m):
                print("", end="")
        except (TypeError, ValueError):
            print("", end="")
    print()
    return (m)
