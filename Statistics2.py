# Percentile Calculation

import numpy as np

data = [10, 20, 30, 40, 50, 60, 70]
print(np.percentile(data,40))


data =[20, 24, 31, 56]
print(np.percentile(data,12))

# Quartile Calculation

data = [10, 20, 30, 40, 50, 60, 70]

print("Q1:", np.percentile(data, 25))
print("Q2:", np.percentile(data, 50))
print("Q3:", np.percentile(data, 75))

# Interquartile Range Calculation

data = [10, 20, 30, 40, 50, 60,70]

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1
print("Interquartile Range:", IQR)  

# outlier detection using IQR

import numpy as np

data = np.array([10, 12, 13, 14, 15, 16, 100])

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data[(data < lower_bound) | (data > upper_bound)]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Outliers:", outliers)
