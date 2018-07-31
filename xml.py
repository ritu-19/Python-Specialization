#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 16:25:20 2018

@author: ritu
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL: ')

uh = urllib.request.urlopen(url)
data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
sum_numbers = 0 
for res in results:
    sum_numbers = sum_numbers + int(res.find('count').text)
   

print(sum_numbers)