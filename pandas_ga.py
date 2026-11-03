import pandas as pd

data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Raj'],
    'Department': ['IT', 'HR', 'IT', 'HR', 'IT'],
    'Salary': [25000, 40000, 50000, 35000, 30000]
}

df = pd.DataFrame(data)
# print(df.groupby('Department')['Salary'].mean())
# print(df.groupby('Department')['Salary'].sum())
# print(df.groupby('Department')['Salary'].count())
# print(df.groupby('Department')['Salary'].max())
# print(df.groupby('Department')['Salary'].min())

print(df.groupby('Department')['Salary'].agg(
    ['sum', 'mean', 'min', 'max', 'count']
))
