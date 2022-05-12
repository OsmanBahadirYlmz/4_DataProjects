# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:35:42 2021

@author: oby_pc
"""

import pandas as pd
import numpy as np
import math 

#1. stddev hesaplama
import statistics
sample =[0.43,0.52,0.35,0.29,0.49]
def uncert (sample):
    
    std=statistics.stdev(sample)
    avg=statistics.mean(sample)
    print("std",std)
    print("avg",avg)
    print("%",std/avg*100)

#2.falling time uncertinity
sample1=[1.55,1.50,1.58,1.49,1.46]
sample2=[1.81,1.93,1.86,1.82,1.80]
sample3=[2.4,2.45,2.47,2.42,2.52]
sample4=[2.96,2.86,2.92,2.90,3.04]
sample5=[3.44,3.46,3.50,3.49,3.42]
sample6=[3.82,3.88,3.86,3.78,3.90]


uncert(sample1)
print("----")
uncert(sample2)
print("----")
uncert(sample3)
print("----")
uncert(sample4)
print("----")
uncert(sample5)
print("----")
uncert(sample6)
print("----")

#3.g hesaplaması- 1.9 metreden düşen R b boyutlarındaki yoyonun t saniye

def calcg(R,b,t):
    l=1.7
    g=(l*((R**2)+(2*(b**2))))/((b**2)*(t**2))
    upper_=(l*((R**2)+(2*(b**2))))
    lower_=((b**2)*(t**2))
    return g,upper_,lower_

#4. yoyonun ivmesi

def ayoyo(R,b):
    a=(2*(b**2)*9.8)/(2*(b**2)+R**2)
    return a
    


def tyoyo (R,b)  :
    l=1.7
    g=9.81
    t=math.sqrt((l*((R**2)+2*(b**2)))/(b**2*g))          
    return t
  


class yoyo ():
    def __init__(self,name,R,b,t):
        self.name=name
        self.R=R
        self.b=b
        self.t=t
        v1=calcg(R,b,t)
        v2=ayoyo(R,b)
        v3=tyoyo(R,b)
        print(self.name)
        print("g","upper","lower",v1)
        print("a",v2)
        print("t",v3)
        
yoyo1=yoyo("yoyo1",0.026,0.008,1.516)
yoyo2=yoyo("yoyo2",0.0345,0.008, 1.844)
yoyo3=yoyo("yoyo3",0.0453,0.008, 2.452)
yoyo4=yoyo("yoyo4",0.0548,0.008, 2.936)
yoyo5=yoyo("yoyo5",0.0659,0.008, 3.46)
yoyo6=yoyo("yoyo6",0.0746,0.008, 3.848)
# yoyo7=yoyo("yoyo7",0.0745,0.006, 4.1)
# yoyo8=yoyo("yoyo8",0.075,0.006, 4.1)


#5. grafikler

#5.1 R out a grafigi
import matplotlib.pyplot as plt
b=0.008
R=np.linspace(0.008,0.15,100)
z=np.linspace(0.008,0.15,100)
g=9.81
a=(2*(b**2)*g)/((2*(b**2))+(z**2))
plt.plot(z,a,label=' ')
plt.title('Outer Radius vs Acceleration')
plt.xlabel('Outer Radius "R"')
plt.ylabel('Acceleration "a"')
plt.grid(alpha=.4,linestyle='--')
# plt.legend()

#R out t grafiği

l=1.7
R2=np.square(R)
t=((l*((R2)+2*(b**2)))/(b**2*g))
t2=np.sqrt(t)
plt.figure(2)
plt.plot(z,t2,label=' ')
plt.title('Outer Radius vs Unwinding Time')
plt.xlabel('Outer Radius "R"')
plt.ylabel('Unwinding time "∆t"')
plt.grid(alpha=.4,linestyle='--')




#R/r grafiği a grafigi
b=R/3
a=(2*(b**2)*g)/((2*(b**2))+(R**2))
plt.figure(3)
plt.plot(z,a,label=' ')
plt.title('Constant Outher Radius and Inner Radius Rate (3) vs Acceleration')
plt.xlabel('Outer Radius "R"')
plt.ylabel('Acceleration "a"')
plt.grid(alpha=.4,linestyle='--')

        