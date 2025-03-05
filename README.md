# APEC2025 - IS10.3 Peter Wilson
Some Examples from the APEC 2025 IS10 Session

## A Simple Example of an Artificial Neural Network to identify parameters for a DC/DC Converter

### makeTrainingdata.py

This Python code will make a dataset for a DC/DC converter with a nominal parameter set of:

- f_sw = 100e3  # Switching frequency (100 kHz)
- V_out = 5  # Output voltage (5V)
- I_out = 1  # Output current (1A)

and generate 1000 samples with design points for L, C and R using a uniform random distribution for each parameter.

The output dataset is then stored in a dataframe within a csv file called "buck_converter_data.csv"

### trainNN.py

This python code will use the previously generated dataset to train a Neural Network to identify suitable values for L,C and R to meet the design specification from the dataset.

A set of test values are defined in this test code to validate the trained neural network, and to plot the training loss function and validation loss function repsectively.
