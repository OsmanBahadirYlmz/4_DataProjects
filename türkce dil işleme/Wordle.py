# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 22:42:27 2022

@author: oby_pc
"""


def read_csv_file(filename):
    """
    Get file name from user and open file content also skip header of csv file
    and returns list of all rows
    if given file name not exisist raise an exception
    """
    
    
    try:
        file_reader = open(filename, "r")
        #skip header
        file_reader.readline()
        #reads all rows in file
        content_reader = file_reader.readlines()
        #close csv file
        file_reader.close()
        return content_reader
        
    except FileNotFoundError as fne:
        print(filename, "does not exist")
        raise fne
        
# tdk=read_csv_file("turkce_kelime_listesi.txt")

def char_analyse(L):
    result={}
    for word in L:
        chars=list(word)
        for char in chars:
            if char in result:
                value=result[char]
                result[char]=value+1
            else:
              result[char] = 1
            
    return result

sozluk=read_csv_file("ortak_kelimeler.txt")


import re


all5words=[]
for line in sozluk:
    line=line.strip()
    line=re.sub("[^a-zA-Z]","     ", line) #remove unwanted charars from list
    if len(line)==5:
        all5words.append(line)
        

analyse1=char_analyse(all5words)


z="abacı"
# file_reader = open("turkce_kelime_listesi.txt", "r")

import pandas as pd
import numpy as np
data=pd.read_csv("ortak_kelimeler.txt")
data2=pd.read_csv("Birleştirilmiş_Sözlük_Kelime_Listesi.txt")
data3=pd.read_csv("TDK_Sözlük_Kelime_Listesi.txt")
data4=pd.read_csv("ortak_kelimeler.txt")
# a=data.iloc[0,0]
# print(len(a))

# sozluk=[]
# for i in range(len(data)):
 
#     if len(data.iloc[i,0])==5:
#         sozluk.append(data.iloc[i,0])
        
        
# sozluk.lower()


