#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list_len = len(my_list)
        my_list.reverse()
        for list in range(my_list_len):
            print("{:d}".format(my_list[list])
