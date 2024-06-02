#!/usr/bin/python3
"""
import csv and json
"""
import csv
import json
"""
conversion de datos csv a json
"""


def convert_csv_to_json(csv_filename):
    """
    convert_csv_to_json
    """
    try:
        data_list = []
        with open(csv_filename, "r") as csv_file:
            data = csv.DictReader(csv_file)
            for elemento in data:
                data_list.append(elemento)

        with open("data.json", "w") as json_file:
            json.dump(data_list, json_file)

        return True
    except FileNotFoundError:
        return False
