#!/usr/bin/python3
def common_elements(set_1, set_2):
    for elementos1 in set_1:
        for elementos2 in set_2:
            if elementos1 == elementos2:
                return set_1 & set_2
