#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for value_ in list_keys:
        if value == a_dictionary.get(value_):
            del a_dictionary[value_]

    return (a_dictionary)
