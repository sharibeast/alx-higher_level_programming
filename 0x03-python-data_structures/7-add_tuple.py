#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple_var = ()
    tpl1 = tuple_a + (0, 0)
    tpl2 = tuple_b + (0, 0)
    new_tuple_var = tpl1[0] + tpl2[0], tpl1[1] + tpl2[1]
    return new_tuple_var
