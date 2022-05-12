# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:01:12 2022

@author: oby_pc
"""

import pandas as pd
import numpy as np
from itertools import repeat

data = pd.read_excel('data.xlsx')
siparis=pd.read_excel('siparis.xlsx')
siparisArray=siparis.values

kod=2181
   
def findDimentions(kod):    
    veri=data[data["Kod No"] ==kod]
    en=float(veri["EN"].values)
    boy=float(veri["BOY"].values)
    
    return (en,boy) 

aa=data["Kod No"]
print(data.EN)
if 1 not in aa.values:
    print("aaaaaa")
    
else :print("bbb")

print(siparisArray[0,0])
      



kod=(siparisArray[0,0])

rectangles = []
for i in range(len(siparisArray)):
    kod=siparisArray[i,0]
    if kod not in 
    adet=siparisArray[i,1]
    enboy=findDimentions(kod)
    rectangles.extend(repeat(enboy,adet))
    print(i)
    