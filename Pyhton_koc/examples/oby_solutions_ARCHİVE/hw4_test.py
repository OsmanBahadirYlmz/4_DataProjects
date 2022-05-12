# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 23:53:33 2022

@author: oby_pc
"""

# filename=input("Enter an input filename: ")
# try:
#     file_reader=open(filename,"r")
# except:
#     print(filename," does not exist")
    


csv="tr_cities.csv"
   



 
file_reader=open(csv,"r")
column_names=file_reader.readline()
contents=file_reader.readlines()



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
        
        
for line in contents:
    line=line.split(",")  
    if line[6]=="capital":
        capital=line[5]
        
destination="final4.csv"
file_write=open(destination,"w")
file_write.write("admin city, number of city, pop \n")
for city,info in dict.items():
    file_write.write(city+","+ str(info[0])+","+str(info[1])+"\n")
           
file_write.close()        
    
    
# dict={"istan":[3,5],"konya":[6,9],5:"bal"}
# # dict["istan"]=

# print(dict.items())    

    
    
    
    
    
    
    
    
   