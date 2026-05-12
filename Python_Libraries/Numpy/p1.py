import numpy as np

array1=np.array([1,2,3,4])
array2=np.array([5,6,7,8])
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
'''print(array1+array2)
print(type(array1))
print(array1.ndim)  # number of dimenstion


print("Dimenstion",a.ndim) # for finding dimenstion

# slicing
print(a[0:2,0:2])''' # array_name[row_Star:row_end:row_step , col_start,col_end,col_step]

#broadcasting (Multiplication).....


#Aggregate function

print(np.sum(a))
print(np.min(a))
print(np.argmin(a))  # position of min value
print(np.sum(a,axis=0))  # 1st column full sum in first position,sec column sum in secod position.....(columnwise) if axis=1 then row

#filters




