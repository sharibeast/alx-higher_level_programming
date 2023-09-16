#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ans = []
    for i in my_list:
        if i % 2 is 0:
            ans = ans + [True]
        else:
            ans = ans + [False]
    return ans
