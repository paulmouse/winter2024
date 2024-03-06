import numpy as np
arr = np.array([[1, 3, 3], [4, 4, 3], [1, 5, 9]])

print(arr)
print(np.rot90(np.rot90(arr)))