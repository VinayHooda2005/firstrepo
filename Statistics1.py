# variace in statistics is a measure of how far a set of numbers are spread out from their average value.

data = [20,31,24,56]
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)
print("Variance =", variance)

import numpy as np
data = [23,31,29,35]
sample_variance = np.var(data, ddof=1)  # ddof=1 for sample variance
print("Sample Variance =", sample_variance)
population_variance = np.var(data)  # default is population variance
print("Population Variance =", population_variance)

# Standard deviation is a measure of the amount of variation or dispersion of a set of values.
data = [23,31,29,35]
standard_deviation = np.std(data)
print("Standard Deviation =", standard_deviation)