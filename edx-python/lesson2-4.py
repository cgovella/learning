#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:14:46 2017

@author: chris
"""

import random
# choice will take a sequence object
random.choice([1,2]) # a coin
random.choice([1,2,3,4,5,6]) # a die
random.choice(range(1,7)) # range will stop before it hits 7
# effectively 1 to 6 like a die. but notice that range is not square bracket

random.choice([range(1,7), range(1,9), range(1,11)])
# will return only one of three ranges

random.choice(random.choice([range(1,7), range(1,9), range(1,11)]))
# will return one of three ranges, then it will take that object
# and run random.choice again!

# 2.4.2
# examples involving randomness

import numpy as np
import matplotlib.pyplot as plt

import random
random.choice([1,2,3,4,5,6])


rolls = []
for k in range(1000000):  # number of times to roll the die
    rolls.append(random.choice([1,2,3,4,5,6])) # take a list, add a new number
plt.hist(rolls, bins = np.linspace(0.5, 6.5, 7))


# y = x1 + x2 + x3 + x4... +x10
ys = []
for rep in range(1000000):
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)
plt.hist(ys);


# 2.4.3


np.random.random()
np.random.random(5) # generate an array
np.random.random((5,3)) # generate a 2d array by giving it a tuple

np.random.normal(0,1) # normal curve with a mean value 0, st dev of 1
np.random.normal(0,1,5) # 1d array
np.random.normal(0,1,(2,5)) #2d array

import time
start_time = time.clock()
X = np.random.randint(1, 7, (1000000, 10))
Y = np.sum(X, axis=1)
plt.hist(Y)
end_time = time.clock()
print(end_time - start_time)


# 2.4.4 time module

import time
start_time = time.clock()
end_time = time.clock()
end_time - start_time 
# returns a float between the two time
# objects. useful for measuring time.

# 2.4.5 random walks

# think about a random walk as a way to model
# movement of a molecule. there is an x and a y displacent.
# you can use a general equation to model the movement.
# you know that at x(t=1) you will be at x(t=0) 
# plus some delta x(t=1). so at x(t=k) you will be at 
# x(t=0) plus the cumulative sum of some delta x(t=k)

X_0 = np.array([[0], [0]])
delta_X = np.random.normal(0, 1, (2, 5)) 
X = np.concatenate((X_0,np.cumsum(delta_X, axis=1)), axis=1)

plt.plot(delta_X[0], delta_X[1], "go")
plt.plot(X[0], X[1], "ro-")
plt.savefig("rw2.pdf")


