#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.
    
    Args:
        obj (object): The object to which the attribute will be added.
        attr (str): The name of the attribute.
        value (any): The value of the attribute.
        
    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
