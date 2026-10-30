import numpy as np
arr = np.array([10, 20, 30, 40, 50])
# arr[4] = 60
# print(arr[4])
# print(arr)

# print(arr[2:4])
# print(arr[2:])
# print(arr[:3])
# print(arr[::3])
# print(arr[::-3])

arr = np.array([
#columns 
#   0-1  1-2  2-3 Rows
    [10, 20, 30],  # 0-1
    [40, 50, 60],  # 1-2
    [70, 80, 90],  # 2-3
    [100, 110, 120]# 3-4
])
# print(arr[1, 1])
# print(arr[1:3,1:2])
print(arr[:,1:3])