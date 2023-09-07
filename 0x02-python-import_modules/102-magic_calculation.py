#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_102_calculation import add, sub

    if a < b:
        ans = add(a, b)
        for number in range(4, 6):
            ans = add(ans, number)
            return (m)
        else:
            return (sub(a, b))
