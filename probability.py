# basic probability 

favorable_outcomes = 3
total_outcomes = 10   

probability = favorable_outcomes / total_outcomes
print("Probability:", probability)  
print("Probability in percentage:", probability * 100, "%")


# Experimental Probability using simulation

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