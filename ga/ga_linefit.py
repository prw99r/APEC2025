from random import randint, random, uniform
from operator import add
import matplotlib.pyplot as plt
import math
import numpy as np
from functools import reduce

def xrange(x):

    return iter(range(x))

def individual(length, min, max):
    'Create a member of the population.'
    return [ randint(min,max) for x in xrange(length) ]

def population(count, length, min, max):
    """
    Create a number of individuals (i.e. a population).

    count: the number of individuals in the population
    length: the number of values per individual
    min: the minimum possible value in an individual's list of values
    max: the maximum possible value in an individual's list of values

    """
    return [ individual(length, min, max) for x in xrange(count) ]

def calcLine(parameters,m):
   """
   Create a line from the parameters supplies and the range
   """
   length = len(parameters)
   line = [0]*2*m
   for i in range(-m,m):
      line[i] = 0
      for p in xrange(length):
         line[i] = line[i] + parameters[p]*math.pow(i,p)
   return line

#
# Still using RMS error
#
def errorRMS(individual,target):
   delta = np.subtract(target,individual)
   delta2 = np.square(delta)
   ave = np.average(delta2)
   dcost = math.sqrt(ave)
   # print "RMS =" + str(dcost)
   return dcost


def fitness(individual, target):
    """
    Determine the fitness of an individual. Higher is better.

    individual: the individual to evaluate
    target: the target parameters that the individuals are aspiring to match
    """
    #m = 100
    targetLine = calcLine(target,m)  
    individualLine = calcLine(individual,m)  
    return errorRMS(individualLine,targetLine)

def grade(pop, target):
    'Find average fitness for a population.'
    summed = reduce(add, (fitness(x, target) for x in pop))
    return summed / (len(pop) * 1.0)

def best(pop, target):
    'Find best (lowest) fitness for a population.'
    theBest = 0
    i = 0
    for x in pop:
      i = i+1
      if fitness(x,target) < theBest:
        theBest = i
    return theBest

def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.1):
    graded = [ (fitness(x, target), x) for x in pop]
    graded = [ x[1] for x in sorted(graded)]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]
    # randomly add other individuals to
    # promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > random():
            parents.append(individual)
    # mutate some individuals
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = randint(
                min(individual), max(individual))
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) / 2
            child = male[:int(half)] + female[int(half):]
            children.append(child)        
    parents.extend(children)
    return parents


# Example usage
target = [.01, 0.5 , -3.0, 5.0, 1.0]
p_count = 100
i_length = 5
i_min = -10
i_max = 10
generations = 100
m = 100

p = population(p_count, i_length, i_min, i_max)
fitness_history = [grade(p, target),]
initial = p[0]
for i in xrange(generations):
    p = evolve(p, target)
    fitness_history.append(grade(p, target))
    print("Generation: " + str(i) + " Fitness = " + str(grade(p,target)))

for datum in fitness_history:
   print(datum)


x = [0]*2*m
index = 0
for i in range(-m,m):
   x[index] = i
   index = index + 1

targetLine = calcLine(target,m)
initialLine = calcLine(initial,m)
finalLine = calcLine(p[0],m)

plt.subplot(131)
plt.title("Initial and Target Function ")
plt.plot(x,targetLine)
plt.plot(x,initialLine,'x')

plt.subplot(132)
plt.title("Optimized Solution and Target")
plt.plot(x,targetLine)
plt.plot(x,finalLine,'x')

plt.subplot(133)
plt.title("Average Fitness of Population")
plt.semilogy(fitness_history)
plt.grid(True)
plt.show()
