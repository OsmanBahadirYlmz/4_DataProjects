# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 23:31:34 2022

@author: oby_pc
"""

file_reader = open("sportivi.csv", "r")
#skip header
# file_reader.readline()
#reads all rows in file
content_1 = file_reader.readlines()
#close csv file
file_reader.close()

file_reader = open("zodiaco.csv", "r")
content_2 = file_reader.readlines()
file_reader.close()
zodiacdict={}
for line in content_2:
    line_lst = line.split(",")
    z_start=int(line_lst[1][3:5]+line_lst[1][0:2])
    z_stop=int(line_lst[2][3:5]+line_lst[2][0:2])
    
    zodiacdict[line_lst[0]]=[z_start,z_stop]
    
keys=list(zodiacdict.keys())

goals={}
for line in content_1:
    line_lst = line.split(",")
    mmdd=int(line_lst[3][3:5]+line_lst[3][0:2])
    goal=int(line_lst[1])
    
    for zodiac in keys:
        if (mmdd>=zodiacdict[zodiac][0] and mmdd<=zodiacdict[zodiac][1]):
            if zodiac in goals:
              goals[zodiac]+=goal
            else:
              goals[zodiac] = goal
        
    

    




