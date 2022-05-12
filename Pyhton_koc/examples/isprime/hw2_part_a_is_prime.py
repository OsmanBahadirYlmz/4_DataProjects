# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:12:18 2021

@author: serda
"""

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

def is_relatively_prime(first, second):
    if first <= 1 and second <= 1:
        return False
    
    if first < second:
        limit = first
    else:
        limit = second
        
    for i in range (2,limit + 1):
        if first % i == 0 and second % i == 0:
            return False
        
   
    return True 






print(is_relatively_prime(9,8)) #true
print(is_relatively_prime(28,49))#false
print(is_relatively_prime(101,103))#true
print(is_relatively_prime(1501,1513))#true




print(is_prime(2))
print(is_prime(1))
print(is_prime(10))
print(is_prime(7))


