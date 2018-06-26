#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:29:00 2018

@author: joby
"""

s = 'azcbobobegghaklbob'

longest = s[0]
current = ''

for start in range(len(s)):
    current = s[start]
    while len(current) + start < len(s) and s[start+len(current)] >= current[-1]:
        current += s[start+len(current)]
    if len(current) > len(longest):
        longest = current
print ("Longest substring in alphabetical order is: " + longest)
