#!/usr/bin/python3
"""
print list sorted
"""


class MyList(list):
    """
    define class
    """
    def print_sorted(self):
        """
        print sorted list
        """
        list_ord = sorted(self)
        print(list_ord)
