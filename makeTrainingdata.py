import numpy as np
import pandas as pd

# Constants
f_sw = 100e3  # Switching frequency (100 kHz)
V_out = 5  # Output voltage (5V)
I_out = 1  # Output current (1A)

# Generate random design points for components
num_samples = 1000
L_values = np.random.uniform(10e-6, 100e-6, num_samples)  # Inductor values (10uH to 100uH)
C_values = np.random.uniform(10e-6, 100e-6, num_samples)  # Capacitor values (10uF to 100uF)
R_values = np.random.uniform(1, 10, num_samples)  # Resistor values (1 to 10 Ohms)

# Simulate ripple and efficiency (using simplified formulas)
delta_I = I_out * 0.2  # 20% current ripple
delta_V = 0.05 * V_out  # 5% voltage ripple
efficiency = 0.9  # Assume a fixed efficiency

# Calculate output ripple voltage and efficiency
V_ripple = (delta_I / (8 * f_sw * C_values))  # Voltage ripple
efficiency_values = 0.85 + 0.1 * np.random.randn(num_samples)  # Add some random variation for efficiency

# Create DataFrame with generated data
data = pd.DataFrame({
    'Inductor (L)': L_values,
    'Capacitor (C)': C_values,
    'Resistor (R)': R_values,
    'Voltage Ripple (V_ripple)': V_ripple,
    'Efficiency': efficiency_values
})

# Save to CSV (optional)
data.to_csv('buck_converter_data.csv', index=False)

print(data.head())
