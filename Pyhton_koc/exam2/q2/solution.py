# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:39:16 2022

@author: oby_pc
"""



def replicate_items(L, k):
    lenght=len(L)
    
    for i in range(lenght):
        for multip in range (k):
           
            L.insert((i+lenght+i*k),L[i])
            
            
       
    for i in range(lenght):
        
        L.pop(0)
        
    return L











l=[8,9,2]
print(replicate_items(l,0))



