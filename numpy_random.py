import numpy as np

# x = np.random.rand()

# x = np.random.randint(1, 1000)
# x = np.random.randint(1, 1000, size=5)
# print(x)

# arr = np.random.random(5)
# arr = np.random.random((2,5))
# print(arr)

# np.random.seed(43)
# print(np.random.randint(1,100, size=5))

rng = np.random.default_rng(42)
# print(rng.integers(1, 100, size=5))

# print(rng.uniform(1, 10, size = 3))
# print(rng.normal(50, 10, size = 3))
# print(rng.binomial(10, 0.5, size = 5))

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# rng.shuffle(arr)
# print(arr)

arr = np.array([1, 2, 3])
print(rng.choice(arr, size=3, replace=True, p=[0, 0.5, 0.5]))