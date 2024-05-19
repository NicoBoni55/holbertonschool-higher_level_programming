#!/usr/bin/python3
def safe_print_integer(value):
    if type(value) is int:
        try:
            print("{:d}".format(value), end="")
        except ValueError:
            return False
        print("")
        return True
