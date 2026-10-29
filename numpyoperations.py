import numpy as np
a = np.array([10, 20, 30 , 40])
b = np.array([1, 2, 3, 4])

# print("Addition:", a + b)
# print("Substraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Power:", a ** 2)

# print("Sum:", np.sum(a))
# print("Mean:", np.mean(a))
# print("Standrad deviation:", np.std(a))
# print("Minimum:", np.min(a))
# print("Max:", np.max(a))

# new_arr = a.reshape(2, 2, 1)
# print(new_arr)

# print("Vertical Stacking:")
# print(np.vstack((b, a)))
# print("Horizontal Stacking:")
# print(np.hstack((b, a)))

# new_arr = np.split(a, 2)
# print(new_arr)

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# print("2D Sum:", np.sum(arr))
# print("2D Sum:", np.sum(arr, axis=0))
print("2D Mean:", np.mean(arr))