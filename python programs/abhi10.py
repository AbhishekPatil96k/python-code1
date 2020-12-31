# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 08:36:35 2020

@author: Abhishek
"""
fptr=open('abhi.txt','r')
data=(fptr.readlines())
print(data)
tlines=len(data)
print(tlines)
wc=0
cc=0
i=0
while(i<=len(data)-1):
    data1=data[i]
    cc1=len(data1)
    wclist=data[i].split()
    wc2=len(wclist)
    wc+=wc2
    cc+=cc1
    i=i+1
print(wc)
print(cc)        
#same program using while loop # 

