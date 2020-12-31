# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:45:39 2020

@author: Abhishek
"""

fptr=open('abhi.txt','r')
print(fptr.name)
print(fptr.mode)
print(fptr.readable())
print(fptr.writable())
print(fptr.closed)
fptr.close()
print(fptr.closed)
