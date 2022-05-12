# -*- coding: utf-8 -*-
"""

"""




# DO NOT CHANGE THE FUNCTION HEADER GIVEN BELOW
def replicate_items(L, k):
   
    # IMPLEMENT THIS FUNCTION BELOW
   
    result=[] #create an empty
    
    if (k==1):
        
        result=L
        return result
    
    
    for i in range(len(L)):
        
        result1=[]
        for j in range (k):
            result1.insert(j,L[i])
        
        result+=result1
        
        
            
            
        
               






    return result












# DO NOT WRITE ANOTHER FUNCTION


