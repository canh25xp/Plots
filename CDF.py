import matplotlib.pyplot as plt
import numpy as np

# Define the values for the CDF
x_values = [-2, -1, -1, 0, 0, 1, 1, 2]
y_values = [0, 0, 0.2, 0.2, 0.7, 0.7, 1, 1]

# Create the plot
plt.figure(figsize=(8, 5))
plt.step(x_values, y_values, where='post', label='CDF')

# Adding the jumps with markers
plt.scatter([-1, 0, 1], [0.2, 0.7, 1], color='red')

# Labeling the plot
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

