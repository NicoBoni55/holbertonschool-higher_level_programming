#!/usr/bin/python3
import os

def generate_invitations(template, attendees):

    path = os.getcwd()
    if os.path.exists(path) == False:
        raise ValueError("path not exist")
    if type(template) is not str:
        raise TypeError("template must be a string")
    if type(attendees) is not list and type(attendees) is not dict:
        raise TypeError("attendees must be a dictionary")
    if not template.strip():
        raise ValueError("Template is empty, no output files generated.")
    if attendees is None:
        raise ValueError("No data provided, no output files generated.")
    else:
        
        expected_keys = ["name", "event_title", "event_date", "event_location"]
        for elements in attendees:
            for key in expected_keys:
                if key not in elements or elements[key] is None:
                    elements[key] = "N/A"
        
        with open("template.txt", "r") as template_file:
            template = template_file.read()
        
        if not template.strip():
            raise ValueError("Template file is empty, no output files generated.")
        
        for X, elements in enumerate(attendees, start=1):
            output = template.format(**elements)
                
            output_numerate = "output_{}.txt".format(X)

            with open(output_numerate, "w") as output_file:
                output_file.write(output)
