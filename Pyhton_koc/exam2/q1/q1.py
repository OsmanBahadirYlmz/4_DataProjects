# -*- coding: utf-8 -*-
"""

"""

# DO NOT CHANGE THE FUNCTION HEADER GIVEN BELOW
def union(A,B):
    #IMPLEMENT THIS FUNCTION
    
    # check size if not correct return a flag
    if not(A["size"]==B["size"]):
        raise Exception("Matrix sizes do not match")
        return
    
    # crete an empy dict to return
    my_union={}
    
    # control evey key in A
    for key in A:
        
        # check if it is on B
        if key in B:
            
            # compere which is lower
            if (A[key]<B[key]):
                
                # print to the key if A is lower
                my_union[key]=A[key]
            else:
                my_union[key]=B[key] #print B value if b is lower
        # if not in b
        else:
            my_union[key]=A[key] #if it is not present in B add A value
            
     # add remaing key which in B.(Has value in B but not present in A)
    for key in B: #check every key
         if key in A:  #if key present in A skip it
             continue
         else:
             my_union[key]=B[key] #if not present in A add to the dict
            
    
    
    return my_union
    
    
#DO NOT WRITE ANY OTHER FUNCTIONS OR CODE BELOW
    
if __name__=='__main__':    
    A={(0, 2): 2, (1, 0): 7, (2, 0): 5, (2, 2): 6, 'size': (2, 3)}
    B={(0, 1): 9, (1, 0): 4, (1, 2): 2, (2, 0): 2, 'size': (3, 3)}
    
    C=union(A,B)
    print(C)
