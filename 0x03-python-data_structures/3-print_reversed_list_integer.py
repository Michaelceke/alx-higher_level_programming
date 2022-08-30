#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for entry in my_list[::-1]:
            print("{:d}".format(entry))
