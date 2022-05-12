# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:53:13 2022

@author: oby_pc
"""


def phone_number_to_digits(phone_str,delimeter=","):
    output=""
    for i in range( len(phone_str)):
        
        if phone_str[i]=="A"or phone_str[i]=="B"or phone_str[i]=="C":
            
            output+="2"
            continue
        if phone_str[i]=="D"or phone_str[i]=="E"or phone_str[i]=="F":
         
            output+="3"
            continue
        if phone_str[i]=="G"or phone_str[i]=="H"or phone_str[i]=="I":
            
            output+="4"
            continue
        if phone_str[i]=="J"or phone_str[i]=="K"or phone_str[i]=="L":
            
            output+="5"
            continue
        if phone_str[i]=="M"or phone_str[i]=="N"or phone_str[i]=="O":
            
            output+="6"
            continue
        if phone_str[i]=="P"or phone_str[i]=="Q"or phone_str[i]=="R"or phone_str[i]=="S":
           
            output+="7"
            continue
        if phone_str[i]=="T"or phone_str[i]=="U"or phone_str[i]=="V":
            
            output+="8"
            continue                  
        if phone_str[i]=="W"or phone_str[i]=="X"or phone_str[i]=="Y"or phone_str[i]=="Z":
            
            output+="9"
            continue
        output+=phone_str[i]
       
        
    return output





























