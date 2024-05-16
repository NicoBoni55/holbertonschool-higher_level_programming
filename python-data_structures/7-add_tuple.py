#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    elem1 = tuple_a[0] + tuple_b[0]
    elem2 = tuple_a[1] + tuple_b[1]
    if (tuple_a or tuple_b < 2):
        if tuple_a[0] == None:
            tuple_a[0] = 0