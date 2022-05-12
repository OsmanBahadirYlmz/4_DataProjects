"""

Created on Sat Jan 15 15:57:30 2022

Serdar  Karaarslan 0075952 section: 03

"""

# DO NOT CHANGE THE FUNCTION HEADER GIVEN BELOW
def build_dictionary(my_list):
   
    # IMPLEMENT THIS FUNCTION BELOW BETWEEN THE DASHED LINES
    # ------------------------------------------------------
    dict={}
    for i in range(50):
        for j in range(len(my_list)):
            if len(my_list[j])==i:
                
                try:
                    dict.update({dict[i]:my_list[j]})
                
                except:
                    dict[i]=my_list[j]
    return dict
                
            
            








    # ------------------------------------------------------
    # IMPLEMENT THIS FUNCTION ABOVE BETWEEN THE DASHED LINES

    
if __name__ == '__main__':
    
    words = ['orange','apple','grape','peanut']
    ret = build_dictionary(words)
    print (ret)
