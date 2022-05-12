# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:06:06 2021

@author: oby_pc
"""

import pandas as pd
import numpy as np
import math 
import statistics


def calcg1(L,T):
    pi42=4*(math.pi**2)
    g=pi42*L/(T**2)
    return g
#data hazırlama
print ("g 2 sayı",calcg1(0.30,1.5))

T1=[1.462,1.434,1.227,1.192,1.256,1.616,2.197]
L1=[0.35,0.30,0.25,0.20,0.15,0.10,0.05]
T2=[1.462,1.434,1.227,1.192,1.256,1.616,2.197]
L2=[-0.35,-0.30,-0.25,-0.20,-0.15,-0.10,-0.05]

# L3=L1[::-1]
# T3=T1[::-1]
T4=[1.462,1.434,1.227,1.192,1.256,1.616,2.197,2.197,1.616,1.256,1.192,1.227,1.434,1.462]
L4=[-0.35,-0.30,-0.25,-0.20,-0.15,-0.10,-0.05,0.05,0.1,0.15,0.2,0.25,0.3,0.35]

X=np.array(L4)
Y=np.array(T4)


#g hesaplamaları
def calcg2(L1,T1):
    result=[]
    for L,T in zip(L1,T1) :
        pi42=4*(math.pi**2)
        g=pi42*L/(T**2)
        result.append(g)
    return result

t=[5,10,55]
r=[2,3,4]

results = [calcg1(x, y) for x,y in zip(L1, T1)]
print (results)

def calcg3(L1,T1):
    pi42=4*(math.pi**2)
    k=0.2
    paran=((k**2)+(L1**2))/((T1**2)+L1)
    g=pi42*paran
    return g

print (calcg3(0.35,1.462))
    
import matplotlib.pyplot as plt


 
#lineear regression
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression
# X=np.array(L4).reshape(-1,1)
# Y=np.array(T4).reshape(-1,1)
# lin_reg = LinearRegression()
# lin_reg.fit(X,Y)

# plt.scatter(X,Y,color='red')
# plt.plot(X,lin_reg.predict(X), color = 'blue')
# plt.title("linear reg")
# plt.show()

# print('Linear R2 degeri')


# polynomial regression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly_reg = PolynomialFeatures(degree = 4)
X2=X.reshape(-1,1)
x_poly = poly_reg.fit_transform(X2)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,Y)
plt.scatter(X,Y,color = 'red')
xval=np.linspace(-0.35,0.35,100).reshape(-1,1)
plt.plot(xval,lin_reg2.predict(poly_reg.fit_transform(xval)), color = 'blue')
plt.title("4 degree poly reg")
plt.show()

#poly reg yarım yarım


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly_reg = PolynomialFeatures(degree = 4)
X2=np.array(L1).reshape(-1,1)
Y=np.array(T1)
x_poly = poly_reg.fit_transform(X2)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,Y)
plt.scatter(X2,Y,color = 'red')
xval=np.linspace(0,0.35,1000).reshape(-1,1)
plt.plot(xval,lin_reg2.predict(poly_reg.fit_transform(xval)), color = 'black')
s1=lin_reg2.predict(poly_reg.fit_transform(xval))
s1=s1.reshape(1000,1)
x1=xval
                    
poly_reg = PolynomialFeatures(degree = 4)
X2=np.array(L2).reshape(-1,1)
Y=np.array(T2)
x_poly = poly_reg.fit_transform(X2)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,Y)
plt.scatter(X2,Y,color = 'red')
xval=np.linspace(-0.35,0,1000).reshape(-1,1)
plt.plot(xval,lin_reg2.predict(poly_reg.fit_transform(xval)), color = 'black')
plt.title("4 degree poly reg")
plt.ylim(1.1,2.3)
plt.show()
s2=lin_reg2.predict(poly_reg.fit_transform(xval))
x2=xval
s1=pd.DataFrame(s1,columns=["T"])
x1=pd.DataFrame(x1,columns=["l"])
s2=pd.DataFrame(s2,columns=["T"])
x2=pd.DataFrame(x2,columns=["l"])
resultpoly1=pd.concat([s1,x1],axis=1)
resultpoly2=pd.concat([s2,x2],axis=1)
resultpoly3=pd.concat([resultpoly1,resultpoly2],axis=0)


#poly2 denemesi 6 10 12 güzel

# mymodel = np.poly1d(np.polyfit(X, Y,12))

# myline = np.arange(-0.35, 0.35 , 0.0001)

# plt.scatter(X, Y, color="r")
# plt.plot(myline, mymodel(myline))
# plt.title("osilation period")
# plt.show()

# a=mymodel(myline)
# a=pd.DataFrame(a,columns=["x"])
# b=pd.DataFrame(myline,columns=["y"])
# s=pd.concat([a,b],axis=1)



#curve fitting

# from scipy.optimize import curve_fit

# def f(x, A, x0, y0):
#     return A * (x - x0)**2 + y0

# def func(x,a,b):
#     return (x**4)* x+a

# xData=np.array(L4)
# yData=np.array(T4)

# plt.plot(xData,yData,"bo", label="exp")

# popt, pcov=curve_fit(func, xData, yData,)
# print(popt)
# xFit=np.arange(-0.40,0.40,0.01)

# plt.plot(xFit,func(xFit,*popt), "r", label="fit")
# plt.title("curve fit")



#cubic spline gekko , çalışmadı

# X=np.array([0,1,2,3,4,5])
# Y=np.array([0.1,0.2,0.3,0.5,1.0,0.9])

# from gekko import GEKKO
# m=GEKKO()
# m.x=m.Param(value=np.linspace(-1,6))
# m.y=m.Var()
# m.cspline(m.x,m.y,X,Y)
# m.options.IMODE=2
# m.solve(disp=False)

# plt.plot(X,Y,"bo",label="data")
# plt.plot(m.x,m.y,'r--' , label="cubic spline")
