# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:09:35 2022

@author: oby_pc
"""


import os

import random
 
 
# Function to create the
# random binary string
def rand_key(p):
   
    # Variable to store the
    # string
    key1 = ""
 
    # Loop to find the string
    # of desired length
    for i in range(p):
         
        # randint function to generate
        # 0, 1 randomly and converting
        # the result into str
        temp = str(random.randint(0, 1))
 
        # Concatenation the random 0, 1
        # to the final result
        key1 += temp
         
    return(key1)
 
# Driver Code
n = 128


file_name = "1.txt"
file_writer = open(file_name, "w")

counter=1
son="H"


while(True):
    try:
        lastfile=int(input("Yazılacak son dosyayı girin: "))
        break
    except:
        print("lütfen uygun bir sayı girin")
        continue
    

while(1):
    
    # b=os.path.getsize("D:\\belgelerim\\programing\\4_Data_Projects\\bigpermutations\\"+file_name)
    
    b=os.path.getsize("D:/belgelerim/programing/4_Data_Projects/bigpermutations/"+file_name)
    
    if (b>500000000):
        file_writer.close()
        
        if (lastfile==counter):
            
            while(True):
               
                try:
                    userinput=int(input("En son yazılan dosya: "+file_name+" dır\n"                                        
                                        "Bundan sonraki yazılacak son dosya numarasını girin\n" 
                                        "Programı sonlandırmak için \"son \" yazın: " ))
                    if (not(userinput>lastfile) ):
                        print("\n *****son dosyadan büyük bir sayı girmelisiniz******* \n")
                        continue
                   
                    lastfile=userinput
                    break   
                                  
                except:
                    print("\n\nlütfen uygun bir sayı girin! ")  
                    son=input("programı sonlarndormak mı istiyorsunuz: E/H?")
                    if (son=="E"):
                        break
                    continue
        if (son=="E"):
            break
        counter+=1
        file_name=str(counter)+".txt"
        file_writer = open(file_name, "w")

        

    file_writer.write(rand_key(n)+"\n")
   
file_writer.close()

    
    


