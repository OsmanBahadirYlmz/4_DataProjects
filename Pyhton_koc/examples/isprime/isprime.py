# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 13:13:05 2021

@author: serda
"""

number = int(input("Enter a number"))


i = 2
is_prime = True
while i < number:
    if number % i == 0:
        is_prime = False
        break    
    i = i + 1
    
    
if is_prime == True:
    print("Prime number")
else:
    print("NOT prime number")