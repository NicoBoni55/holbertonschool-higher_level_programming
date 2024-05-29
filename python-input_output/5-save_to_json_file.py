#!/usr/bin/python3
"""
import json
"""
import json
"""
save to json file
"""


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file
    """
    with open(filename, 'w', encoding='UTF8') as f:
        return json.dump(my_obj, f)
