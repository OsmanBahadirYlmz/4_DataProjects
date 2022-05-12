# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 23:37:00 2022

@author: oby_pc
"""

# x=int(input("sayı gir1:"))
# print (x+1)

# for i in range(5):
#     print("döngü1",i)
#     for j in range(5):
#         print("döngü2",j)
#         break
#     print("döngü3",i)
    
# a=int(13.5)

# no=100
# print (b)
# while True:
#     try:
#         divisor =int(input("integer: "))
#         res=no/divisor
#         break
#     except ValueError as err1:
#         print(err1)
# global a
# def func(a):
    
#     print("function starts")
#     print(a)
#     a=20
#     print("before return")
#     return a
#     print ("after return")
    
    
# def main():
#     a=10
#     b=func(a)
#     print(a)
#     print(b)

# main()    

# name="oby"
# age=15
# no=1
# s="midterm"
# fid=open("nots","w")
# fid.write("first line\n\n")
# fid.write(s+ " "+ str(no))
# fid.close()
# print ("name: %s, age: %d\n" % (name,age))


# ---------------------------
# hw1

# PartA

# year=int(input("enter a year: "))
# if year%4==0 and not(year%100==0) :
#     print("leap year")
# elif year%400==0 :
#     print ("leap year 2")
# else:
#     print ("not leap year")
    

# Part B


# def output(days):
#     print("number of days:",days)
    
# def leapyear(year):
#     if year%4==0 and not(year%100==0) :
#         output(29)
#     elif year%400==0 :
#         output(29)
#     else:
#         output(28)  
# while(1):    
#     month=int(input("enter a month:"))
#     year=int(input("enter a year:"))
    
#     if month in [1,3,5,7,8,10,12] :
#         output(31)
#     if month in [4,6,9,11]:
#         output(30)
#     if month==2:
#         leapyear(year)
        
    
    
# PART C :


# while 1:
#     def output(days):
#         print("number of days:",days)
        
#     def leapyear(year):
#         if year%4==0 and not(year%100==0) :
#             return(29)
#         elif year%400==0 :
#             return(29)
#         else:
#             return(28)  
            
#     def datecheck(month,year): 
        
#         if month in [1,3,5,7,8,10,12] :
#             return(31)
#         elif month in [4,6,9,11]:
#             return(30)
#         elif month==2:
#             return leapyear(year)
#         else:
#             return "invalid date2"
    
    
#     day=int(input("enter a day:"))
#     month=int(input("enter a month:"))
#     year=int(input("enter a year:"))
    
#     if not(0<day<=31):
#         print("invalid Day")
#     if not(0<month<13):
#         print("invalid month")    
#     if year<0:
#         print("invalid year")
#     if (0<day<=31) and (0<month<13) and not(year<0):
#         maxday=datecheck(month,year)
#         if day<=maxday:
#             print ("Valid date")
#         else:
#             print("İnvalid day")
            
            
# part D3

# while(1):
#    def leapyear(year):
#          if year%4==0 and not(year%100==0) :
#              return(29)
#          elif year%400==0 :
#              return(29)
#          else:
#              return(28)
             
#    day=int(input("enter a day:"))
#    month=int(input("enter a month:"))
#    year=int(input("enter a year:"))
#    leap=leapyear(year)
#    passed=0
   
#    for i in range(month):
#        if i in [1,3,5,7,8,10,12] :
#             passed+=31
#        elif i in [4,6,9,11]:
#             passed+=30
#        elif i==2:
#             passed+= leapyear(year)
   
#    passed+=day
#    if 29==leapyear(year):
#        left=366-passed
#    else:
#        left=365-passed
#    print("Days passed: ",passed)
#    print("days remaining",left)
    
 # -------------
# part E



def leapyear(year):
      if year%4==0 and not(year%100==0) :
          return(29)
      elif year%400==0 :
          return(29)
      else:
          return(28)

def leapyear2(year):
      if year%4==0 and not(year%100==0) :
          return(366)
      elif year%400==0 :
          return(366)
      else:
          return(365)


def dleft(day,month,year):
   passed=0 
   for i in range(month):
       if i in [1,3,5,7,8,10,12] :
            passed+=31
       elif i in [4,6,9,11]:
            passed+=30
       elif i==2:
            passed+= leapyear(year)
   
   passed+=day
   if 29==leapyear(year):
       left=366-passed
   else:
       left=365-passed
   return left
   

def dpassed(day,month,year):
   passed=0 
   for i in range(month):
       if i in [1,3,5,7,8,10,12] :
            passed+=31
       elif i in [4,6,9,11]:
            passed+=30
       elif i==2:
            passed+= leapyear(year)
   
   passed+=day
   if 29==leapyear(year):
       left=366-passed
   else:
       left=365-passed
   return passed
   
   
   



while (1):    
   day=int(input("enter curreny day:"))
   month=int(input("enter curreny month:"))
   year=int(input("enter curreny year:"))

   bday=int(input("enter the day of birth day:"))
   bmonth=int(input("enter the day of birth month:"))
   byear=int(input("enter the day of birth year:"))
# validity check
   def datecheck(month,year): 
        
        if month in [1,3,5,7,8,10,12] :
            return(31)
        elif month in [4,6,9,11]:
            return(30)
        elif month==2:
            return leapyear(year)
        else:
            return "invalid date2"
   if not(0<day<=31):
        print("invalid Day")
   if not(0<month<13):
        print("invalid month")    
   if year<0:
        print("invalid year")
   if (0<day<=31) and (0<month<13) and not(year<0):
        maxday=datecheck(month,year)
        if day<=maxday:
            print ("Valid date")
        else:
            print("İnvalid day")

   if not(0<bday<=31):
        print("invalid bDay")
   if not(0<bmonth<13):
        print("invalid bmonth")    
   if byear<0:
        print("invalid byear")
   if (0<bday<=31) and (0<bmonth<13) and not(byear<0):
        maxday=datecheck(month,year)
        if day<=maxday:
            print ("Valid bdate")
        else:
            print("İnvalid bday")

    



   lived1=0
   lived2=0
   lived3=0
   
   lived1=dleft(bday,bmonth,byear)
   lived3=dpassed(day,month,year)
   
   while year>byear+1:
       lived2+=leapyear2(byear+1)
       byear+=1
       
   print("you have lived", lived1+lived2+lived3)
   print("1",lived1)
   print("3",lived3)    
       
























