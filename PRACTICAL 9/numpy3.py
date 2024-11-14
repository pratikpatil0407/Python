import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Element at index 2:", arr[2])

print("Elements from index 1 to 4:", arr[1:4])

arr[2:4] = [300, 400]
print("Modified Array:", arr)
