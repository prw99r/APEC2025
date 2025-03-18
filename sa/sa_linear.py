#
# Simulated Annealing Example - linear array of numbers
# sa_example.py
# P. Wilson (c) 2017
# Lab 6
#
import numpy as np
import math
import random
import matplotlib.pyplot as plt

def acceptance_probability(old_cost, new_cost, T):
   a = math.exp((old_cost-new_cost)/T)
   return a

def anneal(solution,target,alpha,iterations,var):
    old_cost = cost(solution, target)
    cost_values = list()
    cost_values.append(old_cost)
    T = 1.0
    T_min = 0.000001
    while T > T_min:
        i = 1
        while i <= iterations:
            #print("Iteration : " + str(i) + "Cost : " + str(old_cost))
            print("Iteration : " + str(i) + "Target : " + str(target) + "Solution: " + str(solution))
            new_solution = neighbour(solution,var)
            new_cost = cost(new_solution,target)
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random.random():
                solution = new_solution
                old_cost = new_cost
            i += 1
            cost_values.append(old_cost)
        T = T*alpha
    return solution, old_cost, cost_values

def cost(solution,target):
   delta = np.subtract(target,solution)
   delta2 = np.square(delta)
   ave = np.average(delta2)
   dcost = math.sqrt(ave)
   return dcost

def neighbour(solution,d):
   delta = np.random.random((10,1))
   scale = np.full((10,1),2*d)

   offset = np.full((10,1),1.0-d)

   var = np.multiply(delta,scale)
   m = np.add(var,offset)

   new_solution = np.multiply(solution,m)

   return new_solution

   

initial = np.full((10,1),0.5)
target = np.random.random((10,1))

alpha=0.9
iterations = 200
var = 0.01

final_solution, cost, cost_values = anneal(initial,target,alpha,iterations,var)

print(target)
print(final_solution)
print(cost)

plt.subplot(131)
plt.title("Error Function in Simulated Annealing")
plt.plot(cost_values)
plt.grid(True)

plt.subplot(132)
plt.title("Initial")
plt.plot(initial,marker='.')
plt.plot(target)

plt.subplot(133)
plt.title("Final")
plt.plot(final_solution,marker='.')
plt.plot(target)

plt.show()

