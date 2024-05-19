#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dictionary = a_dictionary.copy()
    for keys, values in a_dictionary.items():
        copy_dictionary[keys] = values * 2
    return copy_dictionary
