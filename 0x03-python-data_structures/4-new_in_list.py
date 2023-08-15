#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position without modifying the original list.
    """
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    # Create a copy of the original list to avoid modifying it
    new_list = my_list.copy()
    # Replace the element at the specified index
    new_list[idx] = element
    return new_list
