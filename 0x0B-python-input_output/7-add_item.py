#!/usr/bin/python3
"""
This module contains a script that loads, adds
command line arguments and saves to a python list
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').\
    save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').\
    load_from_json_file


filename = "add_item.json"
my_list = []

for arg in range(len(sys.argv)):
    if arg != 0:
        my_list.append(sys.argv[arg])
save_to_json_file(my_list, filename)
my_list = load_from_json_file(filename)
print(my_list)
