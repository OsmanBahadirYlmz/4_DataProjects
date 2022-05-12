# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 09:52:32 2022

@author: oby_pc
"""

def convertDictionary(IDsNames):
    items=list(dict.items())
    namesIDs={}
    
    for i in range(len(dict)):
        
        if items[i][1] in namesIDs:
          namesIDs[items[i][1]].append(items[i][0])
        else:
          namesIDs[items[i][1]] = [items[i][0]]
    
    
    
    
    return namesIDs




dict={232:"ada",123:"duygu",345:"ınanc",333:"ada",444:"ınanc",34343:"ada"}
newdict=convertDictionary(dict)
