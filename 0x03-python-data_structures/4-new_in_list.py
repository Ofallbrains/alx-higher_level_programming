#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_new_list = my_list.copy()
    len_my_list = len(my_list)
    if idx < 0 or idx >= len_my_list:
        return my_new_list
    my_new_list[idx] = element
    return my_new_list
