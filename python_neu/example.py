# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:53:04 2022

@author: oby_pc
"""
import datetime

class Date:
    month_list=["jan","feb","mar","apr","may","jun","july","aug","sept","oct","now","dec"]
    days_list=["mon","tue","wed","thurs","fri","sat","sunday"]
    
    days=dict(zip(range(0,7),days_list))
    months=dict(zip(range(1,13),month_list))
    
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def day_of_week(self):
        
        
        return datetime.datetime(self.year, self.month, self.day).weekday()
        
    def __str__ (self):
         
         return self.date_format()
     
    def __repr__(self):
         return self.__str__()
     
def date_format(self):
    
    return f"{self.year}/{self.month}/{self.day}"
            
Date.date_format=date_format()

       
a=Date(2022,1,1)

print(a.day_of_week())   






 