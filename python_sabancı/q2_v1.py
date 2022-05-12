# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 09:23:20 2022

@author: oby_pc
"""
# take a city name from user
city=input("please enter city:")

# file read
file_reader=open("unicorns2021.txt","r")
contents=file_reader.readlines()

# counting lines for calculation avarage
linecounter=0

valuation=0

# reading content line by line
for line in contents:
    line=line.split(";")
    if line[4]==city:
        valuation+=int(line[1][1:])
        linecounter+=1
        
avarage=valuation/linecounter
 
print("Avarege of valuation is",avarage,"billion dollars")
 
 
 
Retrieve a city name from user 
read the related document named "unicorns2021.txt"
Initilize temporary variable linecounter and valuation as zero 
perform a for loop until read all lines in document
find lines which contains related city name
get valuation values belong the related city
add valuation to eachother
increase lineconter by 1
calculate avarage by dividing valuation to linecounter



