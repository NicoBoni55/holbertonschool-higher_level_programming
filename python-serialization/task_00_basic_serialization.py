#!/usr/bin/python3
"""
import json
"""
import json
"""
basic serialization
"""


def serialize_and_save_to_file(data, filename):
    """
    serialize_and_save_to_file
    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    load_and_deserialize
    """
    with open(filename, "r") as file:
        datos = json.load(file)
    return datos
