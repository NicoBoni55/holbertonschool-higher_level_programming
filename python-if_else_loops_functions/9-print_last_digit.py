#!/usr/bin/python3
def print_last_digit(number):
    new_number = abs(number) % 10
    print("{}".format(new_number), end="")
    return(new_number)
