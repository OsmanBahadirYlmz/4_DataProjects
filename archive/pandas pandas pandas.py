# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 02:33:27 2021

@author: oby_pc
"""


import numpy as np 
import pandas as pd 



n = int(input())
data=[]
for i in range(n):
    data.append(input().split())

import pandas as pd



datax=0
datay=0
cluster1=[]
cluster2=[]
for i in range (n):
    datax=float(data[i][0])
    datay=float(data[i][1])
    dist1=(datax-0)**2+(datay-0)**2
    dist2=(datax-2)**2+(datay-2)**2
  
    if dist1<=dist2:
        cluster1.append(data[i])
    else : 
        cluster2.append(data[i])

df1=pd.DataFrame(cluster1)
df2=pd.DataFrame(cluster2)


print("df1")
print(df1)
print("df2")
print(df2)


a=round(df1.mean(axis=0),2)
b=df2.mean(axis=0)
c=a.values.tolist()
print(a.values.tolist())
print(b.values.tolist())
print(type(c))















