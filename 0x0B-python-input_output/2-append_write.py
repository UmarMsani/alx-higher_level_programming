#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF-8) and return the number of characters added.

    :param filename: The name of the file to be appended.
    :type filename: str, optional
    :param text: The text to be appended to the file.
    :type text: str
    :return: The number of characters added.
    :rtype: int
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    return num_chars_added
