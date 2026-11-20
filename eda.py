import pandas as pd
import numpy as np

data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Vijay',
             'Neha', 'Rohan', 'Pooja', 'Karan', 'Anjali'],
    'Age': [25, 30, 28, 35, 40, 26, 32, 29, 45, 31],
    'Salary': [25000, 45000, 35000, 60000, 75000,
               30000, 50000, 40000, 90000, 55000],
    'Experience': [1, 5, 3, 10, 15, 2, 7, 4, 18, 6],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT',
                   'HR', 'Finance', 'IT', 'Finance', 'HR'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Male',
               'Female', 'Male', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)
# print(df)
print(df.head(2))
print(df.tail(3))
print("Rows:", df.shape[0])
print("Cols:", df.shape[1])
print(df.info())
print(df.columns)
print(df.describe())
print(df.describe(include='object'))
