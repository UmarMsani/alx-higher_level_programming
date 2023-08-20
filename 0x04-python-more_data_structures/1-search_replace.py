#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
        A function that traverse through a list for an element that matches
        search and modify it with replace then returns a new list.
        @elem: Elements
    '''
    new_list = []

    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    
    return new_list
