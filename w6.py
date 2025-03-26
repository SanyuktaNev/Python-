import numpy as np

data = [10, 20, 30, 40, 50]
m = max(data)
print(m)

mean_value = np.mean(data)
print("Mean:", mean_value)

result_exp = np.exp(data)
print(result_exp)

arr = np.array([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
result_sin = np.sin(arr)
result_cos = np.cos(arr)