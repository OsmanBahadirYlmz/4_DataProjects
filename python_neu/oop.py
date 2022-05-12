# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 00:42:02 2022

@author: oby_pc
"""

class Circle():
    Pi=3.14 #class attribute
    def __init__(self,radius):
        self.radius=radius
        self.area=self.pi*radius*radius
    def circum(self): #class method
        return 2*self.pi*self.radius
    
    
