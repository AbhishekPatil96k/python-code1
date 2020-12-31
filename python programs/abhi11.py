# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:11:54 2020

@author: Abhishek
"""
fptr=open('abhi.txt','r')
data=fptr.readlines()
print(data)
print(len(data))
twords=0
tchar=0
for line in data:
    charcount=len(line)
    wordlist=line.split()
    wordcount=len(wordlist)
    tchar=tchar+charcount
    twords+=wordcount
print(twords)
print(tchar)