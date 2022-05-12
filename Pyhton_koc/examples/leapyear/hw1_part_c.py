# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:32:45 2021

@author: serda
"""

day = int(input("Enter a day : "))
month = int(input("Enter a month : "))
year = int(input("Enter a year : "))

is_valid_day = False
if month == 1:
    if day > 0 and day <= 31:
        is_valid_day = True

elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        if day > 0 and day <= 29:
            is_valid_day = True
           
    else:
        if day > 0 and day <= 28:
             is_valid_day = True
                 
elif month == 3:
    if day > 0 and day <= 31:
        is_valid_day = True
        
elif month == 4:
    if day > 0 and day <= 30:
        is_valid_day = True
elif month == 5:
    if day > 0 and day <= 31:
        is_valid_day = True  
elif month == 6:
    if day > 0 and day <= 30:
        is_valid_day = True
elif month == 7:
    if day > 0 and day <= 31:
        is_valid_day = True
elif month == 8:
    if day > 0 and day <= 31:
        is_valid_day = True
elif month == 9:
    if day > 0 and day <= 30:
        is_valid_day = True
elif month == 10:
    if day > 0 and day <= 31:
        is_valid_day = True
elif month == 11:
    if day > 0 and day <= 30:
         is_valid_day = True
elif month == 12:
    if day > 0 and day <= 31:
        is_valid_day = True
else:
    if day > 0 and day <= 31:
        is_valid_day = True       
        
is_valid_month = False
if month >= 1 and month <= 12:
    is_valid_month = True

is_valid_year = False
if year > 0:
    is_valid_year = True
   


if is_valid_day == False:
    print("Invalid day")

if is_valid_month == False:
    print("Invalid month")
    
if is_valid_year == False:
    print("Invalid year")
    
    
if is_valid_day == True and is_valid_month == True and is_valid_year == True:
    print("Valid date")
