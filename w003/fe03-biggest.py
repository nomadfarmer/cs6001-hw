#!/usr/bin/env python3
"""
Function biggest should take a dictionary as an argument. Each value
in the dictionary should be a list. Our function should return key which
has the most values associated with it -- the longest list.
"""

__author__ = "Joby/Nomadfarmer"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    d = {'b': [1], 'c': [2, 3, 4], 'd': [5, 6]}

    if biggest(d) == 'c':
        print("good")
    else:
        print("bad")


def biggest(a_dict):
    longest_key = None
    longest_length = 0
    for k in a_dict.keys():
        if len(a_dict[k]) > longest_length:
            longest_length = len(a_dict[k])
            longest_key = k
    return longest_key

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
