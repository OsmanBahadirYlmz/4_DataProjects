# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 21:32:41 2021

@author: oby_pc
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("data.xlsx")
falltime=df.iloc[:,6]
R=df.iloc[:,0]

plt.scatter(R,falltime)
