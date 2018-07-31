#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 23:09:39 2018

@author: ritu
"""


import re

f = open("actual.txt")

sum_numbers = 0
# Open file
numbers = re.findall(r'[0-9]+', f.read())
#print(numbers)

for num in numbers:
    #print(num)
    sum_numbers = sum_numbers + int(num)

print(sum_numbers)


#sum_numbers = (int(num) for num in (re.findall(r'[0-9]+', f.read())))
print(sum((int(num) for num in (re.findall(r'[0-9]+', f.read("actual.txt"))))))