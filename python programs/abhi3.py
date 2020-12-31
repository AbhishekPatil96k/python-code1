# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 19:49:41 2020

@author: Abhishek
"""

def fun1():
    print('hi bhau')
    
def fun2(x,y):
    z=x+y
    print(z)
def display(ptr1,ptr2):
    ptr1()
    x=60
    y=70
    ptr2(x,y)
yo1=fun1
yo2=fun2
yo1()
c=30
d=30
yo2(c,d)
yo2(30,30)
display(yo1,yo2)
