# 1D array

import numpy as np;
arr=np.array([23,46,57,89,76])
print(arr)
print(len(arr))
print(type(arr))
print(arr[2])
print(arr[:3])

arr[2]=25
print(arr)
print(arr.dtype)
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr[0]+arr[2])


# 2D array

array=np.array([[12,34,56,43],[23,56,78,98]])
print(array)
print(array.ndim)
print(array[1,2])
print(array[0,-1])
print(array[0,-3:-1])


# 3D array
arr=np.array([[[12,34,65,78],[23,67,89,84]],[[31,52,45,94],[46,39,57,17]]])
print(arr)
print(arr.ndim)
print(arr[1,0,2])
x=arr.copy()
arr[1,0,2]=98
print(arr)
print(x)