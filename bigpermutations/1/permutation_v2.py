# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:06:17 2022

@author: oby_pc
"""
import sys
from itertools import permutations


for group in permutations(['111001','111010','111011','111100','111101','111110','1111'], 16):
    # print(''.join(group))  
    print(group)
    print("a")
