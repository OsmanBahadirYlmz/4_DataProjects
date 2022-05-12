# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 23:18:04 2022

@author: oby_pc
"""

import pandas as pd
import matplotlib as plt
import seaborn as sns # for plotting graphs
import datetime as dt
import numpy as np

data=pd.read_excel("data1.xlsx")
# data.FİRMA.value_counts()[:10].plot(kind="bar")
# data.isnull().sum(axis=0)
print(data.iloc[1,15])


# calculate some parameters
data2=data.groupby('FİRMA').agg({'YIL': lambda date: (date.max() - date.min()).days,
                                        'InvoiceNo': lambda num: len(num),
                                        'Quantity': lambda quant: quant.sum(),
                                        'TotalPurchase': lambda price: price.sum()})


data2=data.groupby('FİRMA')
purchase_number={}
for i in range (2218):
    firm_name=data.iloc[i,1].lower()
    if firm_name in purchase_number:
      purchase_number[firm_name]+=1
    else:
      purchase_number[firm_name] =1
   
         
    
    date=data.iloc[i,15]
    # if data.iloc[i,11]:
    #     value=
    

