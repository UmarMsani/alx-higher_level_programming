#!/usr/bin/python3

import json

def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file, using a JSON representation.

    :param my_obj: The object to be serialized and saved to the file.
    :param filename: The name of the file to save the JSON representation.
    :type filename: str
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
