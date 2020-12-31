# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 09:08:14 2020

@author: Abhishek
"""

print('enter the file name')
data=input()
str=open(data,'a')
for i in range(5):
    print('enter the name')
    name=input()
    print('enter the id')
    unique=input()
    print('enter the Place')
    place=input()
    print('enter the phone')
    phone=input()
    str.write(name+' '+unique+' '+place+' '+phone+' '+'\n')
str.close()
print('employees written in file')
