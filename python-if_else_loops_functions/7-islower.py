#!/usr/bin/python3
def islower(c):
    lower = ord(c)
    if (lower <= 97) and (lower >= 122):
        return True
    else:
        return False
