import numpy as np

arr = np.array([10, 20, 30 ,40, 50])
print(arr)
print(type(arr))

arr = np.array(
    [
        [
            [
                [1, 2, 3],
                [4, 5, 6],    
            ],
            [
                [4, 5, 6],
                [7, 8, 9]
            ]
        ],
        [
            [
                [1, 2, 3],
                [4, 5, 6],    
            ],
            [
                [4, 5, 6],
                [7, 8, 9]
            ]
        ]
    ]
)
# print(arr)
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Data type:", arr.dtype)
print(arr[0, 0, 1, 0])

arr = np.array([
            [
                [1, 2, 3],
                [4, 5, 6],    
            ],
            [
                [4, 5, 6],
                [7, 8, 9]
            ]
        ])
print(arr + 10)
print(arr * 2)

arr = np.zeros((2, 3, 4))
print(arr)
print(arr.shape)
print(arr.size)