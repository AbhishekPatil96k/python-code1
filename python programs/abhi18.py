# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 11:18:44 2020

@author: Abhishek
"""

def print_msg():
    print('hello everyone')
def outer(print1):
    print('inside outer function')
    def inner():
        print('inside inner')
        ref=print1 
        ref()
    return inner  
ptr1=outer(print_msg)
ptr1() 
 
    
