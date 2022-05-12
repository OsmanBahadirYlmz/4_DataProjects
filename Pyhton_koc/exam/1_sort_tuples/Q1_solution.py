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
    # print(indexlist)
    
    for j in range(len(L)) : 
                     
        for i in indexlist:
            # print("j+i",j,i)
            
            if (L[i][selectedIndex]<minindex):
                minindex=L[i][selectedIndex]
                minlist=L[i]
                i_value=i #++++++++ eklenmeli kaçmış
                # print("if çağrıldı")
                # print("minindex,minlist,",minindex,minlist,i_value)
        newlist.append((minlist))
        indexlist.remove(i_value) #++++++++ pop-remove
        # print("newlist",newlist)
        # print("indexlist",indexlist)
        minindex=9999 #++++++++ eklenmeli kaçmış
    print(newlist)
    return newlist


sort_tuples([(7,8,3),(3,7,5),(9,1,4),(7,6,2)], 0)
sort_tuples([(7,8,3),(3,7,5),(9,1,4),(7,6,2)], 1)
sort_tuples([(7,8,3),(3,7,5),(9,1,4),(7,6,2)], 2)



    # ------------------------------------------------------
    # IMPLEMENT THIS FUNCTION ABOVE BETWEEN THE DASHED LINES
    # DO NOT WRITE ANY STATEMENT OUTSIDE sort_tuples()
    