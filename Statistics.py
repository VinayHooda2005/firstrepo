# This program calculates the mean of a list of numbers

data=[20,31,24,56]
mean=sum(data)/len(data)
print("Mean =",mean)

# in Numpy we calculate the mean using the mean() function

import numpy as np
data =[20,31,24,56]
mean =np.mean(data)
print("Mean =",mean)

# median is the middle value of a list of numbers

import numpy as np
data = [20,31,24,56]
median = np.median(data)
print("Median =",median)

data = [20,10,40,50,80]
median =np.median(data)
print("Median =",median)

# mode is the most frequently occurring value in a list of numbers

from statistics import mode, multimode
data = [20,31,24,56,31,24]
print("Mode =",mode(data))
print("Multimode =",multimode(data))

# range in statistics is the difference between the largest and smallest values in a list of numbers

data = [20,31,24,56]
range = max(data) - min(data)
print("Range =",range)