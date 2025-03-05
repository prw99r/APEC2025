import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv('buck_converter_data.csv')

# Features: L, C, R (Inductor, Capacitor, Resistor)
X = data[['Inductor (L)', 'Capacitor (C)', 'Resistor (R)']].values

# Labels: Voltage Ripple and Efficiency
y = data[['Voltage Ripple (V_ripple)', 'Efficiency']].values

# Normalize the data (standard scaling)
scaler_X = StandardScaler()
X_scaled = scaler_X.fit_transform(X)

scaler_y = StandardScaler()
y_scaled = scaler_y.fit_transform(y)

# We use StandardScaler to normalize the input features and output labels to have zero mean and unit variance. This helps the neural network train faster and improve convergence.
 
# Define and Train the Neural Network
# Now we’ll define a simple neural network using Keras (part of TensorFlow) to predict voltage ripple and efficiency based on the component values.

import tensorflow as tf
from tensorflow.keras import layers, models

# Build the neural network model
model = models.Sequential([
    layers.InputLayer(input_shape=(X_scaled.shape[1],)),  # 3 input features
    layers.Dense(64, activation='relu'),  # Hidden layer with 64 units
    layers.Dense(32, activation='relu'),  # Another hidden layer
    layers.Dense(2)  # Output layer with 2 values: V_ripple and Efficiency
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
history = model.fit(X_scaled, y_scaled, epochs=100, batch_size=32, validation_split=0.2)

# Evaluate the model
loss = model.evaluate(X_scaled, y_scaled)
print(f"Model Loss: {loss}")

# Evaluate the Model
# Once the model is trained, you can evaluate it using new test data (or by splitting the dataset into training and testing sets).

# Predict on new data
X_test = np.array([[50e-6, 20e-6, 5]])  # New sample: L=50uH, C=20uF, R=5 Ohms
X_test_scaled = scaler_X.transform(X_test)  # Normalize the test data

# Predict
y_pred_scaled = model.predict(X_test_scaled)

# Inverse transform the predicted values back to original scale
y_pred = scaler_y.inverse_transform(y_pred_scaled)

print(f"Predicted Voltage Ripple: {y_pred[0][0]}")
print(f"Predicted Efficiency: {y_pred[0][1]}")

# Visualize the Results
#You can plot the loss during training to see how well the model is converging.
import matplotlib.pyplot as plt

# Plot training and validation loss
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title('Training and Validation Loss')
plt.show()

