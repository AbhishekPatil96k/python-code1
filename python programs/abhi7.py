# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:42:15 2020

@author: Abhishek
"""

def even(num):
    if(num%2==0):
        return True
    else:
        return False
i=0
l=[]
while(i<=4):
    print('enter the element')
    num=int(input())
    l.insert(i,num)
    i=i+1
i=0
while(i<=4):
    data=l[i]
    status=even(data)
    if(status==True):
        print(data)
    i=i+1
    
    

