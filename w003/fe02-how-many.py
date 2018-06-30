#!/usr/bin/env python3
"""
Function how_many should take a dictionary as an argument. Each value
in the dictionary should be a list, according to the sketchy specs. Our
function should return the total number of elements of all of those
lists.
"""

__author__ = "Joby/Nomadfarmer"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    print("This exercise isn't meant to be run from the command line... sorry!")

def test_how_many():
    d = {'b': [1], 'c': [2, 3, 4], 'd': [5, 6]}
    assert(how_many(d) == 6)
    d['d'].pop()
    assert(how_many(d) == 5)
    d['elephant'] = ['6', '7', '8', '9', '10']
    assert(how_many(d) == 10)

def how_many(a_dict):
    count = 0
    for l in a_dict.values():
        count += len(l)
    return count

if __name__ == "__main__":
    main()
