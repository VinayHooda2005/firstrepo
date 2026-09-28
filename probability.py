#  Basic Probability in python 

favourable = 3
total = 6

probability = favourable / total

print("Probability:", probability)
print("Percentage:", probability * 100)


# Experimental probability using simulation

import random

heads = 0
total = 1000

for i in range(total):
    result = random.choice(["Heads", "Tails"])

    if result == "Heads":
        heads += 1

probability = heads / total

print("Heads:", heads)
print("Experimental Probability:", probability)


# Probability with Numpy

import numpy as np

data = np.array([1, 2, 3, 4, 5, 6])

even = np.sum(data % 2 == 0)
total = len(data)

probability = even / total

print("Probability of even number:", probability)