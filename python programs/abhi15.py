# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:34:09 2020

@author: Abhishek
"""
#closer concept
def outer():
    print('i am inside outer function')
    def inner():
        print('i am inside inner function')
        print(inner)
    return inner
ref=outer()
print(ref)
ref()

