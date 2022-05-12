# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

word=input("please enter a word:")

# generate filenames
for i in range(1001):
    filename=str(i+1)+".txt"
    
    
    # reading allfiles
    file_reader=open(filename,"r")
    content=file_reader.readlines()
    
    # searching word
    line_index=1
    for line in content:
        if word in line:
            print("file:",filename,"Line #:",line_index)
        
        line_index+=1
        
        
        