# -*- coding: utf-8 -*-
"""

"""

# YOU MAY WRITE OTHER FUNCTIONS AND USE THEM IN THE FUNCTION BELOW
# IMPLEMENT YOUR ADDITIONAL FUNCTIONS BELOW, IF YOU HAVE ANY

#check recursively number add
def check_add(L,i):
    if (i<len(L)):
        return L[i]
    else:
        return L[i]+check_add(L,i)
#check recursively number sub
def check_sub(L,i):
    if (i<len(L)):
        return L[i]
    else:
        return L[i]-check_sub(L,i)



# DO NOT CHANGE THE FUNCTION HEADER GIVEN BELOW
def N_sum(L,N):
    
    # IMPLEMENT THIS FUNCTION BELOW

    for i in range(len(L)):
       result= check_add(L,i)
       if(result==N):
           print("")
           return 
       result=check_sub(L, i)
       if(result==N):
           print("")
           return
        
        
        
        



    
    print("NOT FOUND")

    return






















