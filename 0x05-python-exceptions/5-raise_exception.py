#!/usr/bin/python3

def raise_exception():
    try:
        x = "string" + 5  # This will raise a TypeError
    except TypeError as e:
        raise e
