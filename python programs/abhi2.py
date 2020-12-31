# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 19:39:51 2020

@author: Abhishek
"""

def fun1():
    print('hi bhau')
def fun2(x,y):
    z=x+y
    print(z)
fun1()
a=2
b=5
fun2(a,b)
ptr1=fun1
ptr2=fun2
ptr1()
ptr2(8,8)

    