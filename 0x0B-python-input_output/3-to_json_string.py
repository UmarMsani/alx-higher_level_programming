#!/usr/bin/python3

import json

def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    :param my_obj: The object to be serialized.
    :return: The JSON representation of the object.
    :rtype: str
    """
    return json.dumps(my_obj)
