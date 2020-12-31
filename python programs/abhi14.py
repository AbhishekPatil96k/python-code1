# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:27:27 2020

@author: Abhishek
"""

fptr=open('abhi.txt','r')
pos=fptr.tell()
print(pos)
print(fptr.read(50))
pos=fptr.tell()
print(pos)
fptr.seek(15)
pos=fptr.tell()
print(pos)

