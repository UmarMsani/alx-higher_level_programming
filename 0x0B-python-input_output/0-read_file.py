#!/usr/bin/python3
"""This defines a text file-reading function."""


def read_file(filename=""):
    """
    Read and print the content of a text file (UTF-8) to stdout.

    :param filename: The name of the file to be read.
    :type filename: str, optional
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
