# -*- coding: utf-8 -*-
"""

Created on Sat Jan 15 15:57:30 2022

Serdar  Karaarslan 0075952 section: 03

"""
import numpy as np
file_reader = open("input.csv", "r")
dimention=file_reader.readline().split(",")

content= file_reader.readlines()
for line in content:
    line_lst = line.split(",")
    
print(dimention[1])
my_array=np.zeros((int(dimention[0]),int(dimention[1])))
print (line_lst[0])
my_array[2][2]=5
# my_array2=np.zeros((int(dimention[0]),int(dimention[1])))
a=my_array.shape
b=a[1]