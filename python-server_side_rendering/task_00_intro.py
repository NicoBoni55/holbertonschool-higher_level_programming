#!/usr/bin/python3
import os

def generate_invitations(template, attendees):

    if type(template) != str:
        raise TypeError("template must be a string")
    if type(attendees) != dict:
        raise TypeError("attendees must be a dictionary")
    if template is None:
        raise ValueError("Don´t have a template")
    if attendees is None:
        raise ValueError("Don´t have a attendees")
    else:
        for element in attendees:
            element_name = element.get("name")
            element_event_title = element.get("event_title")
            element_event_date = element.get("event_date")
            element_event_location = element.get("event_location")    
        
        element_name.replace()