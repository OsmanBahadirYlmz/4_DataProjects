# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:53:13 2022

@author: oby_pc
"""

def retes():
    file_reader=open("currency","r")
    
    column_names=file_reader.readline()
    content=file_reader.readlines()
    list=[]
    for line in content:
        line=line.split("\t")
        
        highest=0
        value=0
        for word in range(line):
            if word>highest:
                highest=word
                
        value=highest       
        
    return value
    


a=retes()





























