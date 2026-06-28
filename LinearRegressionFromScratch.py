import numpy as np

# Step 1: Create Dataset
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Step 2: Calculate Mean
mean_x = np.mean(x)
mean_y = np.mean(y)

# Step 3: Calculate Slope (m)
numerator = np.sum((x - mean_x) * (y - mean_y))
denominator = np.sum((x - mean_x) ** 2)

m = numerator / denominator

# Step 4: Calculate Intercept (c)
c = mean_y - (m * mean_x)

# Step 5: Predict Values
y_pred = m * x + c

# Step 6: Calculate Mean Squared Error
mse = np.mean((y - y_pred) ** 2)

# Display Results
print("Slope (m):", m)
print("Intercept (c):", c)
print("Predicted Values:", y_pred)
print("Mean Squared Error:", mse)


#Visualization

import matplotlib.pyplot as plt

plt.scatter(x, y, label="Actual Data")
plt.plot(x, y_pred, color="red", label="Regression Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression from Scratch")
plt.legend()
plt.show()
