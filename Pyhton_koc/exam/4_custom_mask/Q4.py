"""



Serdar  Karaarslan 0075952 section: 03

"""

import numpy as np

def custom_mask(arr,n):
    '''This function takes an ndarray (arr) and an integer (n) 
    as parameters. It returns an ndarray to be used as a custom mask.
    The mask array has the same dimensions as arr. 
    Mask elements are True, if their row (i) and column (j) indeces satisfy
    the equation (i + j) % n == 0, and False otherwise'''
    # DO NOT CHANGE THE CODE ABOVE THIS LINE
    
    # IMPLEMENT THIS FUNCTION
    # finding shepe of array
    shape=arr.shape
    
    # define a boolean np array 
    my_array=np.full(shape, True, dtype=bool)
    
    # changing value of mask one by one
    for i in range(shape[0]):
        for j in range(shape[1]):
            if (i+j)%n==0:
                my_array[i][j]=bool(True)
            else:
                my_array[i][j]=bool(False)
                
                
                
    
    
    
    return my_array

# DO NOT CHANGE THE CODE BELOW THIS LINE
if __name__ == '__main__':
    arr = np.ones((4,6))
    print('Original array')
    print(arr)

    n = 5
    mask = custom_mask(arr,n)
    print('\nCustom mask')
    print(mask)

    arr[mask] = 0
    print('\nUpdated array')
    print(arr)

