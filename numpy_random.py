import numpy as np

# x = np.random.rand()

# x = np.random.randint(1, 5)
# x = np.random.randint(1, 100, size=3)
# print(x)

# arr = np.random.random(5)
# arr = np.random.random((2,3))
# print(arr)

# np.random.seed(42)
# print(np.random.randint(1,100, size=5))

rng = np.random.default_rng()
# print(rng.integers(1, 200, size=5))

# print(rng.uniform(1, 10, size =5))
# print(rng.normal(0, 10, size =5))
# print(rng.binomial(10, 0.5, size =5))

arr = np.array([1, 2, 3, 4, 5])
# rng.shuffle(arr)
# print(arr)

print(rng.choice(arr, size=3, replace=False))