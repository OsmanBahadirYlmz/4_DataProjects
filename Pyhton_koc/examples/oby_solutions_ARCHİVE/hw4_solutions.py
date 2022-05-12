# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 23:53:33 2022

@author: oby_pc
1:50
"""
def get_content():
    filename=input("Enter an input filename: ")
    try:
        file_reader=open(filename,"r")
        column_names=file_reader.readline()
        content=file_reader.readlines()
        return content
    except:
        print(filename," does not exist")
    
def create_dict(contents):
    dict={}
    
    for line in contents:
        line=line.split(",")
        try:
            pop=int(line[7])
        except:
            pop=0
      
       
        if line[5] not in dict:
            dict[line[5]]=[1,pop]
        else:
            val=dict[line[5]]
            dict[line[5]]=[val[0]+1,val[1]+pop]
                
    


def main():
    contents=get_content()
    create_dict(contents)
    
main()
    