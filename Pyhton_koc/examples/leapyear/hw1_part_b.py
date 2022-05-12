# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:17:47 2021

@author: serda
"""

month = int(input("Enter a month : "))
year = int(input("Enter a year: "))
if month == 1:
    print(31)
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        print(29)
    else:
        print(28)
elif month == 3:
    print(31)  
elif month == 4:
    print(30)  
elif month == 5:
    print(31)   
elif month == 6:
    print(30) 
elif month == 7:
    print(31) 
elif month == 8:
    print(31) 
elif month == 9:
    print(30) 
elif month == 10:
    print(31)
elif month == 11:
    print(30)
elif month == 12:
    print(31)    
    