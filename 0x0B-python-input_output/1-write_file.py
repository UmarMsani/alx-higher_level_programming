#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the number of characters written.

    :param filename: The name of the file to be written.
    :type filename: str, optional
    :param text: The text to be written to the file.
    :type text: str
    :return: The number of characters written.
    :rtype: int
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
