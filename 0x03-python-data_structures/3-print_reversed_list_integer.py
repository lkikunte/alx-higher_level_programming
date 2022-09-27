#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    index = list_len - 1
    while index >= 0:
        print("{}".format(my_list[index]))
        index -= 1
