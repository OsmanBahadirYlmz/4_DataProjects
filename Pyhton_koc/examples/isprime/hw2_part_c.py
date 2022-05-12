# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:14:23 2021

@author: serda
"""
import hw2_part_a as A

def calculate_n_and_phi():
    p = int(input("first prime number:"))
    while p < 0 or not A.is_prime(p):
        p = int(input("Invalid prime, enter again:"))
    q = int(input("second prime number:"))
    while q < 0 or not A.is_prime(q):
        q = int(input("Invalid prime, enter again:"))
    
    return p * q, (p-1) * (q - 1)   
     



print(calculate_n_and_phi())