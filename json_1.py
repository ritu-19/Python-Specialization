#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 09:01:46 2018

@author: ritu
"""
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

uh = urllib.request.urlopen(url, context=ctx)
#print('ul ' , uh)
data = uh.read().decode()
#print('Retrieved', len(data), 'characters')
#print(data)
info = json.loads(data)
#print('Comments:', len(info))

#print("Type :   " , type(info))
sum_numbers = 0
for item in info:
    #sum_numbers = sum_numbers + int(item['count'])
    #print(info[item])
    if item == 'comments':
        for i in info[item]:
            sum_numbers = sum_numbers + int(i['count'])
            
print(sum_numbers)
   