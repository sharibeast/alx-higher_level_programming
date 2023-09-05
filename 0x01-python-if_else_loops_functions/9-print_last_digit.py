#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number = number * -1
    lst_dgt = number % 10
    print("{}".format(lst_dgt), end='')
    return (lst_dgt)
