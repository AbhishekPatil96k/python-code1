# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:46:53 2020

@author: Abhishek
"""

print('enter file name')
data=input()
fptr=open(data,"a")
for i  in range(5):
    print('enter the name ')
    name=input()
    fptr.write(name+'\n')
fptr.close()
print('5 times written')    
