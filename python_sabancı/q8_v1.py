# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 09:28:03 2022

@author: oby_pc
"""

def sum_even(mylist):
    mysum=0
    for i in range(len(mylist)):
        if mylist[i]%2==0:
            mysum+=mylist[i]
        
    return mysum

lst1=[3,2,4,5]
lst2=[2,3,6,6,5,7]
print(sum_even(lst2))