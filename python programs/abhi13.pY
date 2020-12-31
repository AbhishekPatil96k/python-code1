# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:29:14 2020

@author: Abhishek
"""

ptr=open("IMG_20200803_123755_111.jpg","rb")
imagedata=ptr.read()
#print(imagedata)
ptr1=open('myCar.jpg','wb')
ptr1.write(imagedata)
print('image created successfully')
ptr.close()
ptr1.close()
