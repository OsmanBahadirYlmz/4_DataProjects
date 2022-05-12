# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 15:52:11 2021

Serdar  Karaarslan 0075952 section: 03

this program adds employees to given employee list if he/she is not in list and
removes employee from employee list if name parameter is in list and displays all
employees and also displays an employee which is given in name parameter if in 
employee list 
"""

def add_employee(employee_list, name, phone, room):
    #loop all employees
    for i in range(len(employee_list)):
        #if found the name , gives an error message
        if name.upper() == employee_list[i][0].upper():
            print("(error in add) ", name, "already exists")
            return # if found finishes the function
        
    # end of loop create tuple
    data = (name , phone, room)
    #appends tuple to employee list
    employee_list.append(data)
    
def remove_employee(employee_list, name):
    #loop all employees
    for i in range(len(employee_list)):
         #if name had found, removes it from employee list
        if name.upper() == employee_list[i][0].upper():
            employee_list.remove(employee_list[i])
            return # finishes the function
    
    # end of loop if not found the employee prints error message
    print("(error in remove)", name, "is not found")
    
    
def display_all(employee_list):
    # employee list has an employee
    if len(employee_list) > 0:
        i = 0
        while i < len(employee_list): # loop all employees
            print(employee_list[i][0],",", employee_list[i][1], ",", employee_list[i][2])
            i += 1
    else: # if list is empty
        print("--EMPTY--")
        
        
def show_employee(employee_list, name):
    # loop all employees
    for i in range(len(employee_list)):  
        # if name parameter equals the list of tuples's name prints
        if name.upper() == employee_list[i][0].upper():
            print("name = " , employee_list[i][0])
            print("office =", employee_list[i][2])
            print("tell = ",employee_list[i][1] )
            return
        
    #if not found prints error message  
    print("(error in show)", name, "is not found")
    
