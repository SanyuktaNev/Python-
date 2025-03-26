import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, c='blue', marker='o')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

plt.show()