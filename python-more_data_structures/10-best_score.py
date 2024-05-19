#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        valor_max = max(a_dictionary.values(), default=None)
        for llave, valor in a_dictionary.items():
            if valor == valor_max:
                return llave
