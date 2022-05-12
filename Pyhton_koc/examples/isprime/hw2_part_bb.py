# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:45:16 2021

@author: serda
"""

def display_menu():
    while True:
        print("g or G for key generation")
        print("e or E for encryption")
        print("d or D for decryption")
        print("x or X to exit")
        print()
    
        choice = input("Please enter your choice:")
        print()
        
        if choice == "g" or choice == "G" or \
            choice == "e" or choice == "E" or \
            choice == "d" or choice == "D" or \
            choice == "x" or choice == "X":
            return c
        else:
            print("***Invalid option***")
        
        
        
display_menu()