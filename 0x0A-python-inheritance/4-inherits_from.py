#!/usr/bin/python3
"""This defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class; otherwise False.
    
    Args:
        obj (object): The object to check.
        a_class (class): The specified class to compare against.
        
    Returns:
        bool: True if obj is an instance of a class that inherited from a_class, False otherwise.
    """
    return issubclass(type(obj), a_class)
