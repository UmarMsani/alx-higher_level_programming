#!/usr/bin/ptyhon3

import json

def from_json_string(my_str):
    """
    Return an object (Python data structure) represented by a JSON string.

    :param my_str: The JSON string to be deserialized.
    :type my_str: str
    :return: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
