#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for elemento in my_list:
        if elemento == search:
            new_list.append(replace)
        else:
            new_list.append(elemento)
    return (new_list)
