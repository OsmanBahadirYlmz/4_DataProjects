# DO NOT CHANGE THE FUNCTION HEADER GIVEN BELOW
def sort_tuples(L, selectedIndex): 
   
    # IMPLEMENT THIS FUNCTION BELOW BETWEEN THE DASHED LINES
    # ------------------------------------------------------
    minindex=9999999
    
    indexlist=list(range(0,len(L)))
                   
    for i in indexlist:
        if (L[i][selectedIndex]<minindex):
            minindex=i
    print (L[minindex])
    indexlist.pop(minindex)








    # ------------------------------------------------------
    # IMPLEMENT THIS FUNCTION ABOVE BETWEEN THE DASHED LINES
    # DO NOT WRITE ANY STATEMENT OUTSIDE sort_tuples()
    