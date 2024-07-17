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
    if template is None:
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
        
        for X, elements in enumerate(attendees, start=1):
            output = template.format(**elements)
                
            output_numerate = "output{}.txt".format(X)
            for index in range(1, len(attendees) + 1):
                if os.path.exists(output_numerate):
                    print("index exist{}".format(index))
                else:
                    print("where is the index?") 

            with open(output_numerate, "w") as output_file:
                output_file.write(output)


with open('template.txt', 'r') as file:
    template = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template, attendees)