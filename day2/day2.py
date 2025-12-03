#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 19:18:36 2025

@author: dougcallahan
"""

import sys

with open('./day2_input.txt') as f: 
#with open('./day2_input_test.txt') as f: 
#with open('./' + sys.argv[1]) as f: 
    input_ls = [ x for x in f.readline().split(',')]
    
    input_ls = [ ( int(x.split('-')[0]), int(x.split('-')[1]) ) for x in input_ls]
    
print("Part I: ")

s = 0    
    
for item in input_ls: 
    
    start, end = item
    
    for x in range(start, end + 1):
        x = str(x)
        if len(x) % 2 == 0:
            l = int(len(x)/2)
            if x[0:l] == x[l:]:
                s += int(x)

print(s)

print("Part II: ")

s = 0 

for item in input_ls: 
    
    start, end = item
    
    for x in range(start, end + 1):
        str_x = str(x)
        len_x = len(str_x) 
        
        for i in range(1, len_x):
            if (len_x % i) == 0:
                mult = int( len_x / i )
                if str_x == str_x[0:i] * mult:
                    s += x
                    break 

print(s)    