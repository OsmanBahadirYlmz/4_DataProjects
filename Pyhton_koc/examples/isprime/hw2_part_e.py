# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:44:24 2021

@author: serda
"""

def generate_private_key(e, n, phi):
    m = 0
    
    while ((1 + m * phi) % e) != 0:
        m += 1
        
    d = (1 + m * phi) / e
    

    return int(d), n





d1, n1 = generate_private_key(7, 10403, 10200)
print(d1, n1)

d2, n2 = generate_private_key(7, 3233, 3120)
print(d2, n2)

d3, n3 = generate_private_key(5, 323, 288)
print(d3, n3)