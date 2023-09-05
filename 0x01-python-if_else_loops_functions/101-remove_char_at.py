#!/usr/bin/python3
def remove_char_at(str, n):
    custom_string = ''
    for i in range(len(str)):
        if i != n:
            custom_string += str[i]
    return (custom_string)
