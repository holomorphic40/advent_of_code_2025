#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 17:35:04 2025

@author: dougcallahan
"""

import sys 

basedir = '/Users/dougcallahan/advent/2025/'

## Part 1:

with open(basedir + sys.argv[1]) as f: 
#with open(basedir + 'day1_input_test1.txt') as f: 
    input_ls = [ (x[0], int(x[1:])) for x in f.readlines() ]

def process_tup( tup ):
    direction, dist = tup
    
    if direction == 'L': 
        return -1*dist
    else: 
        return dist 
    
start = 50 

ctr = 0

for tup in input_ls: 
    start += process_tup(tup)
    
    if start % 100 == 0:
        ctr += 1
        

print("Part I: ", ctr)

## Part 2:
  
start = 50 

ctr = 0

for tup in input_ls: 
    
    end = start + process_tup(tup)
    
    start_hundreds, end_hundreds = start // 100, end // 100
    
    diff = abs( end_hundreds - start_hundreds)
    
    if ( (end % 100) == 0) and (tup[0] == 'L'):
        diff += 1    
    if ( (start % 100) == 0) and (tup[0] == 'L'):
        diff -= 1
    
    ctr += diff
        
    start = end 
        
print("Part II: ", ctr)

## Part 2, again: 
    
start = 50 

ctr = 0

for tup in input_ls: 
    
    if tup[0] == 'L':
        for _ in range( abs(tup[1])):
            start -= 1
            if (start % 100) == 0:
                ctr += 1
    
    if tup[0] == 'R':
        for _ in range( abs(tup[1])):
            start += 1
            if (start % 100) == 0:
                ctr += 1

print("Part II, again: ", ctr)





