# array shape

import numpy as np;
arr=np.array([12,34,56,78,54])
print(arr.shape)

arr=np.array([[34,56,74,31],[98,71,56,63]])
print(arr.shape)

arr=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(arr.shape)

# array reshape

arr=np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4))

print(arr.reshape(2,2,2))
print(arr.reshape(-1))