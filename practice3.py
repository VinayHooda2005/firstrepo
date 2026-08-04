import numpy as np

                                        #=================================
                                        #      NUMPY PRACTICE QUESTIONS
                                        #=================================

#Question 2 : function to create numpy array
np.array(2)
print("==============")

#Question 3 : numpy array containing numbers from 1 to 10
arr=np.arange(1,11)
print(arr)
print("==============")

#Question 4 : even number from 1 to 20 
arr=np.arange(1,21,2)
print(arr)
print("==============")

#Question 5 : array from the list [10,20,30,40,50]
arr=np.array([10,20,30,40,50])
print(arr)
print("==============")

#Question 6 : print datatype of array
arr=np.array([10,20,30,40,50])
print(arr.dtype)
print("==============")

#Question 7 : find number of elements
arr=np.array([10,20,30,40,50])
print(arr.size)
print("==============")

#Question 8 : 2D array
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print("==============")

#Question 10 : array of zeros of size 5
arr=np.zeros(5)
print(arr)
print("==============")

                                    #===============================================
                                    #       Shape and Reshape of Numpy Arrays
                                    #===============================================

#Question 12 : find shape of np.array ([[1,2,3,],[4,5,6]])
arr=np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print("==============")

#Question 13 :array from 1 to 12 and reshape it into a 3*4 matrix
arr=np.arange(1,13).reshape(3,4)
print(arr)
print("==============")

#Question 14 : reshape np.range(1,13) into a 2*6 matrix
arr=np.arange(1,13).reshape(2,6)
print(arr)
print("==============")

#Question 16 : convert a 1D array into a 2D using reshape()
arr=np.array([1,2,3,4,5,6])
arr2=arr.reshape(2,3)
print(arr2)
print("==============")

#Question 17 : 4*2 matrix using reshape()
arr=np.arange(1,9).reshape(4,2)
print(arr)
print("==============")

#Question 18 :print both original shape and reshaped shape 
arr=np.arange(1,13)
print("Original Shape :",arr)

arr2=arr.reshape(3,4)
print("Reshaped Shape :",arr2)
print("==============")
                                            #========================================
                                            #       Joining and Splitting of Arrays
                                            #========================================
#Question 19 :
#np.concatenate()
print("==============")

#Question 20 : Join arr1=[1,2,3] and arr=[4,5,6]
arr1=np.arange(1,4) 
arr2=np.arange(4,7)
arr3=np.concatenate((arr1,arr2))
print(arr3)
print("==============")

#Question 21 : join 2D arrays vertically
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
c=np.concatenate((a,b),axis=0)
print(c)
print("==============")

#Question 22 : join 2D arrays horizontally
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
c=np.concatenate((a,b),axis=1)
print(c)
print("==============")


#Question 24 : split a NumPy array
#np.split()

#Question 25 : soplit np.array([1,2,3,4,5,6]) into 3 parts
arr=np.array([1,2,3,4,5,6])
arr_split=np.split(arr,3)
print(arr_split)
print("==============")

#Question 26 : split an array into 4 equal parts
arr=np.array([1,2,3,4,5,6,7,8])
arr_split=np.split(arr,4)
print(arr_split)
print("==============")  
