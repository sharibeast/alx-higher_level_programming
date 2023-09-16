#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        return (sum([a * b for a, b in my_list])/sum(y for x, y in my_list))
    return 0
