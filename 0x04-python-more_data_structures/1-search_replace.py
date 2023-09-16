#!/usr/bin/python3
def search_replace(mylist, search, replace):
    created_list = []
    for x in mylist:
        if x == search:
            created_list.append(replace)
        else:
            created_list.append(x)
    return created_list
