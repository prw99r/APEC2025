# 1. A Simple Example of an Artificial Neural Network to identify parameters for a DC/DC Converter

## 1.1 Files used
makeTrainingdata.py

trainNN.py

## 1.2 makeTrainingdata.py

This Python code will make a dataset for a DC/DC converter with a nominal parameter set of:

- f_sw = 100e3  # Switching frequency (100 kHz)
- V_out = 5  # Output voltage (5V)
- I_out = 1  # Output current (1A)

and generate 1000 samples with design points for L, C and R using a uniform random distribution for each parameter.

The output dataset is then stored in a dataframe within a csv file called "buck_converter_data.csv"

## 1.3 trainNN.py

This python code will use the previously generated dataset to train a Neural Network to identify suitable values for L,C and R to meet the design specification from the dataset.

A set of test values are defined in this test code to validate the trained neural network, and to plot the training loss function and validation loss function repsectively.

When the Neural Network is run using python:

python trainNN.py

The resulting training and validation response is plotted, along with a printed message that provides the final error and values achieved in the terminal window

## 1.4 Training and Validation Losses

Example of running over 100 epochs:

* Model Loss: 0.4750613570213318
* Predicted Voltage Ripple: 0.012823262251913548
* Predicted Efficiency: 0.8310545086860657

![image](https://github.com/user-attachments/assets/10527308-08f1-4ea9-af79-de00f40282b6)
