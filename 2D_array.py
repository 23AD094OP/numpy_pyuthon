import numpy as np
a = np.array([[2,3,4,5,6],[2,3,4,5,6]])
print(a)
a.ndim 
# indexing value
b =a[1,4]
print(b)
# get specfic row
c =  a[0,:]
print(c)
# get specfic column
d = a[:,2]
print(d)
# to make all the enteries in 2nd column as 5
a[:,2] = 5
print(a)
# to change that column alone
a[:,2] = [2,3]
print(a)