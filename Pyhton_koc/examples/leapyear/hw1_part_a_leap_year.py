# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 10:57:22 2021

@author: serda
"""

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
    print("leap year")
else:
    print("Not leap year")    
