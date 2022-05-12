# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:55:33 2022

@author: oby_pc
"""

usage=int(input())
city=input()


if (usage<300 and usage>=0):
    baseprice=3

elif (usage<600 and usage>=300):
    baseprice=7
    
elif (usage>=600):
    baseprice=15
    
    
    
if(city=="istanbul"):
    baseprice+=3
    
elif(city=="ankara"):
    baseprice+=2

else:
    baseprice-=1


bill=usage*baseprice

print("%.2f" %bill)



