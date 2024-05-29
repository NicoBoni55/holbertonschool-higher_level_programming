#!/usr/bin/python3
"""
import json
"""
import json
"""
create an object from JSON
"""


def load_from_json_file(filename):
    """
    load_from_json_file
    """
    with open(filename, 'w', encoding='UTF8') as f:
        return json.dumps(f)
