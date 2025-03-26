import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 2, 8, 6]

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='^', linestyle='-', color='b', label='Data Point')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot Example')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(x, y, color='g', alpha=0.7, label='Data Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Plot Example')
plt.legend()
plt.grid(True)
plt.show()
