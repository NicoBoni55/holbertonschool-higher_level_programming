#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    contador = 0
    for elementos in range(x):
        try:
            print("{:d}".format(my_list[elementos]), end="")
        except IndexError:
            break
        contador += 1
    print("")
    return contador
