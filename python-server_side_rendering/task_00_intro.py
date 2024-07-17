#!/usr/bin/python3
import os

def generate_invitations(template, attendees):

    path = os.getcwd()
    if os.path.exists(path) == False:
        print("path not exist")
        return
    if not isinstance(template, str):
        print("template must be a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(elem, dict) for elem in attendees):
        print("attendees must be a dictionary")
        return
    if not template():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print ("No data provided, no output files generated.")
        return
        
    expected_keys = ["name", "event_title", "event_date", "event_location"]
    for elements in attendees:
        for key in expected_keys:
            if key not in elements or elements[key] is None:
                elements[key] = "N/A"
        
    with open("template.txt", "r") as template_file:
        template_content = template_file.read()
        
    if not template_content():
        raise ValueError("Template file is empty, no output files generated.")
        
    for X, elements in enumerate(attendees, start=1):
        output = template.format(**elements)
                
        output_numerate = "output_{}.txt".format(X)

        with open(output_numerate, "w") as output_file:
            output_file.write(output)
