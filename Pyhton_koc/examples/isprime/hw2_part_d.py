# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:30:46 2021

@author: serda
"""

import hw2_part_a as A

def generate_public_key(n, phi):
    e = 2
    
    while e < phi:
        if A.is_relatively_prime(e, phi):
            break
        e += 1
        
        
    return e, n


e1, n1 = generate_public_key(10403, 10200)
print(e1, n1)

e2, n2 = generate_public_key(3233, 3120)
print(e2, n2)

e3, n3 = generate_public_key(323, 288)
print(e3, n3)

    