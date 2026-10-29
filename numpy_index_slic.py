import numpy as np
arr = np.array([10, 20, 30, 40, 50])
# print(arr[5])

# print(arr[1:2])
# print(arr[1:])
# print(arr[:3])
# print(arr[::2])
# print(arr[::-2])

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
# print(arr[2, 2])
# print(arr[1:3,:])
print(arr[:,1:3])