"""

Created on Sat Jan 15 15:57:30 2022

Serdar  Karaarslan 0075952 section: 03

"""


import numpy as np

def read_array(infile):
    '''This function reads the array data from a CSV file.
    The filename is received as the parameter infile.
    The first line of the CSV file contains 
    the row and column numbers for the array. 
    The remaining lines contain the row (i) and column (j) indices 
    and the value (v) for all nonzero elements as i,j,v.
    The function returns an ndarray where the nonzero elements 
    are set according to the data in infile. 
    All other elements are set to zero.'''
    
    # DO NOT CHANGE THE CODE ABOVE THIS LINE
    
    # IMPLEMENT THIS FUNCTION
    import numpy as np
    # read document
    file_reader = open(infile, "r")
    # find dimentions
    dimention=file_reader.readline().split(",")
    
    # reading values
    content= file_reader.readlines()

        
    # define an zero array with dim
    my_array=np.zeros((int(dimention[0]),int(dimention[1])))
    
    
    # read the content one by by
    for line in content:
        line_lst = line.split(",")
        # change the zero values to expected value 
        x=int(line_lst[0])
        y=int(line_lst[1])
        val=int(line_lst[2])
        my_array[x][y]=val
        
    print (my_array)
            
    
    
    
    
    
    
    return

# DO NOT CHANGE THE CODE BELOW THIS LINE

if __name__ == '__main__':
    arr = read_array('input.csv')
    print(arr)
