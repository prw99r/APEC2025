Example 2. A Simple Example of optimization of a power grid using simulated annealing optimization

## 2.1 Files used
sa_example.py

## 2.2 sa_example.py

This Python code will take a grid of power demand and then try and optimize a power supply matrix to match the demand grid

The algorithm is a simulated annealing algorithm using the following process:

![image](https://github.com/user-attachments/assets/f5e99262-695b-4626-bb36-cfc20fde3959)

## 2.3 Running the code

To run the code use the following command:

python sa_example.py

The simulated annealing optimizer will start with a blank set of supply data and then us the optimizer to match to a random grid of demand figures, plotting the starting and finishing matrices using a graphical display, and plotting the overall error of the set number of iterations (100):

![image](https://github.com/user-attachments/assets/de46e673-c08f-42d1-9874-0f3e5b0410dc)
