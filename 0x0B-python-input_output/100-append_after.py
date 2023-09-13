#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific string in a file.

    :param filename: The name of the file.
    :type filename: str, optional
    :param search_string: The specific string to search for in each line.
    :type search_string: str
    :param new_string: The line of text to insert after the matching lines.
    :type new_string: str
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
