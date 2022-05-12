"""

Created on Sat Jan 15 15:57:30 2022

Serdar  Karaarslan 0075952 section: 03

"""


# DO NOT CHANGE THE FUNCTION HEADER GIVEN BELOW
def sort_tuples(L, selectedIndex): 
   
    # IMPLEMENT THIS FUNCTION BELOW BETWEEN THE DASHED LINES
    # ------------------------------------------------------
    minindex=9999999
    newlist=[]
    indexlist=list(range(0,len(L)))
    for j in range(len(L)) :              
        for i in indexlist:
          
            if (L[i][selectedIndex]<minindex):
                minindex=i
                minlist=L[i]
               
        newlist.append((minlist))
        indexlist.pop(minindex)
    print(newlist)
    return newlist


sort_tuples([(7,8,9),(3,7,5),(9,1,4),(7,6,2)], 0)
sort_tuples([(7,8,9),(3,7,5),(9,1,4),(7,6,2)], 1)
sort_tuples([(7,8,9),(3,7,5),(9,1,4),(7,6,2)], 2)



    # ------------------------------------------------------
    # IMPLEMENT THIS FUNCTION ABOVE BETWEEN THE DASHED LINES
    # DO NOT WRITE ANY STATEMENT OUTSIDE sort_tuples()
    