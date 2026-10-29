import numpy as np
a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [5, 6],
    [7, 8]
])

# print(a)
# print(b)
# print(np.dot(a, b))
# print(a @ b)
# print(a.T)

# det = np.linalg.det(a)
# print(det)
# inverse = np.linalg.inv(a)
# print(inverse)

# values, vectors = np.linalg.eig(a)
# print(values)
# print(vectors)

c= np.array([5, 6])

solution = np.linalg.solve(a, c)
print(solution)