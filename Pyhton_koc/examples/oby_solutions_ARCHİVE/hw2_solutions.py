# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 00:15:23 2022

@author: oby_pc
12:24

04:36

"""
# This function takes an integer as its parameter and returns True if the
# integer is prime and returns False otherwise. You may assume that its
# parameter is always a positive integer.
def is_prime(number):
    prime = True
    if number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set flag to True
                prime = False
                # break out of loop
                break

# check if flag is True
    if prime and number>1:
            return True
    else:
        return False



# This function takes two integers (first and second) as its parameters and
# returns True if these two integers are relatively prime and returns False
# otherwise. Remember that two integers are relatively prime if they share
# no common factors other than 1. You may assume that both of the parameters
# are always positive integers.
# def is_relatively_prime(first, second):
    
def is_relatively_prime(first, second):
    if first<second:
        first,second=second,first
    rprime=True    
    for i in range (2,first+1):
        if first%i==0 and second%i==0:
            rprime=False
            
    if rprime and first>1 and second>1:
            return True
    else:
        return False    
            


# Options are explained above. Please check the given output for the menu format.
def display_menu():
    
    while(True):
        print("g or G for key generation")
        print("e or E for encryption")
        print("d or D for decryption")
        print("x or X to exit \n")
           
        selection=str(input("please enter our choice: ")  ) 
        if selection=="g" or selection=="G":
            selection="G"
            break
        elif selection=="e" or selection=="E":
            selection="E" 
            break
        elif selection=="d" or selection=="D":
            selection="D"
            break
        elif selection=="x" or selection=="X":
            selection="X"
            break
        else:
            print("\n ***Invalid option*** \n")
            continue
        
    return selection











