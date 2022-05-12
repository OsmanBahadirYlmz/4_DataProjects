# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 14:58:41 2022

@author: oby_pc
"""

def add_employee(employee_list, name, phone, room):
    if len(employee_list)==0:
        employee_list.append([name,phone,room])
        return employee_list
    else:    
        for  i in range(len(employee_list)):
           
            if name.upper() == employee_list[i][0].upper():
                print("(error in add) ",name," already exists")
                return
    employee_list.append([name,phone,room])
    return employee_list
    
    
def remove_employee(employee_list, name):
    popindex=-1
    for  i in range(len(employee_list)):
        if name.upper() == employee_list[i][0].upper():
            popindex=i
            
            employee_list.pop(popindex)
            return employee_list
        
    print("(error in remove) ",name," is not found")





def display_all(employee_list):
    try:
        if len(employee_list)==0:
            print("--EMPTY--")
        for i in range(len(employee_list)):
            print(employee_list[i][0]," , ",employee_list[i][2]," , ",employee_list[i][1])
    except:
        print("--EMPTY--")        
    return
def show_employee(employee_list, name):
    nameindex=-1
    for  i in range(len(employee_list)):
        if name.upper() == employee_list[i][0].upper():
            nameindex=i
    if nameindex==-1:
        print("(error in show) ",name," is not found")
        return
    print("name: ",employee_list[nameindex][0])
    print("office: ",employee_list[nameindex][2])      
    print("tel: ",employee_list[nameindex][1])
    
 
    
 
    
 
    
 
