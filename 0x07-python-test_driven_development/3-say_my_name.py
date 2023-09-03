#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    # Check if both first_name and last_name are strings
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    
    # Print the name
    full_name = "My name is {} {}".format(first_name, last_name)
    print(full_name)
