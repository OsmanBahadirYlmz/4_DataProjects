# -*- coding: utf-8 -*-
"""
Created on Sun May  2 23:10:24 2021

@author: oby_pc
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from PIL import Image
img = Image.open('poyraz_256.jpg')
imgGray = img.convert('L')
imgGray.save('poyraz256_gray.jpg')
pix_val = list(imgGray.getdata())
pix_val=np.array(pix_val)
pix_val=pix_val.reshape(256,256)
plt.imshow(pix_val,cmap="gray")

# # gauss calculation
# a=np.arange(-2,3,1)
# b=np.arange(-2,3,1)
# def gauss2d (a,b):
#   out=1/(2*math.pi)*math.e**(-(a**2+b**2)/2)
#   return out

# for i in a :
#   for j in b:
#     result=gauss2d(i,j)
#     #print ("x:",i,",","y:",j,"=",result)
#     print ("f({},{})={}".format(i,j,result.round(5)))

# print(pix_val)

# pix_val16=pix_val[0:16,0:16]

# new_img=np.zeros((16,16))
# new_img[0,0]=189
# new_img[0,1]=187
# plt.imshow(new_img,cmap="gray")

# karnel=np.zeros((5,5))
# for i in a :
#   for j in b:
#     result=gauss2d(i,j)
#     #print ("x:",i,",","y:",j,"=",result)
#     print ("f({},{})={}".format(i,j,result.round(5)))
#     karnel[i+2,j+2]=result.round(5)


# new_picture=np.zeros((252,252))
# for row in range (252):
#   for column in range (252):
#     sum=0
#     for i in range(5):
#       for j in range(5):
#         conv=karnel[i,j]*pix_val[i+row,j+column]
#         sum+=conv
#     new_picture[row,column]=sum/(0.98179)
    
# plt.imshow(new_picture,cmap="gray") 

# pix_val16_n=new_picture[0:16,0:16]
# pix_val16_n=np.around(pix_val16_n,0)
# plt.imshow(pix_val16_n,cmap="gray") 