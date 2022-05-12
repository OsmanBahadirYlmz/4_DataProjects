# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:01:55 2021

@author: oby_pc
"""
import math 
import statistics
a=3.47
print (a*1.03, a*0.97)
print(a*1.)
    
b=[3.44,3.42,3.50,3.52,3.40]
print ("mean" , statistics.mean(b))

# print((0.0005-1.7)/1.7*100)
print("R unc",(0.0001/0.0746*100))
print("g hatası",(10.5-9.81)/9.81*100)
# print(0.008**2*1.516**2)

# unc of falling time


#upper uncert calculation
l=0.029
R=0.38
R2=[0.38,0.28,0.22,0.18,0.15,0.13]

b=1.25
for i in R2:
    unc=l+(2*i+(2*b))
    print("uncupper", unc)

#lower uncert calc
b=1.25
t=3.18
t2=[3.18,2.88,1.89,2.33,0.96,1.27]
for i in t2:
    unc2=(2*b)+(2*i)
    print("unclow",unc2)

#grafik çizme

y_val=[0.001366,0.002241,0.003706,0.005322,0.007600,0.009678]
x_val=[0.000147,0.000217,0.000384,0.000551,0.000766,0.000947]

import matplotlib.pyplot as plt


x=[0,0.0011]
a2=0.0011*9.81
y=[0,a2]
plt.plot(x,y, label="Theoretical g ")
# y_err=[0.0001366,0.0002241,0.0003706,0.0005322,0.0007600,0.0009678]
# x_err=[0.0000147,0.0000217,0.0000384,0.0000551,0.0000766,0.0000947]
x_err=[8.86,8.26,6.27,7.16,4.42,5.04]
x_err2=[a*b/100 for a,b in zip(x_val,x_err)]


y_err=[3.28,3.08,2.96,2.88,2.82,2.78]
y_err2=[a*b/100 for a,b in zip(y_val,y_err)]

plt.errorbar(x_val,y_val, ecolor="r", xerr=x_err2, yerr=y_err2,fmt=".k", capsize=3, label="Calculated g")
plt.title('Theoretical "g" and Calculated "g" ')
plt.xlabel('b^2 (∆t^2)')
plt.ylabel('l(R^2+2b^2)')
plt.legend()
print(0.009678/0.000947)
