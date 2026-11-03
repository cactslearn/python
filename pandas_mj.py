import pandas as pd

df1 = pd.DataFrame({
    'Emp_ID': [1, 2, 3, 4, 5, 6],
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Raj', 'Ammy'],
})

df2 = pd.DataFrame({
    'Emp_ID': [1, 2, 3, 4, 5, 7],
    'Salary': [25000, 40000, 50000, 35000, 30000, 10000]
})

# print(pd.merge(df1, df2, on='Emp_ID', how='inner'))
# print(pd.merge(df1, df2, on='Emp_ID', how='left'))
# print(pd.merge(df1, df2, on='Emp_ID', how='right'))
# print(pd.merge(df1, df2, on='Emp_ID', how='outer'))

df3 = pd.DataFrame({
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Raj', 'Ammy']
},index=[1, 2, 3, 4, 5, 6])
df4 = pd.DataFrame({
    'Salary': [25000, 40000, 50000, 35000, 30000, 10000]
}, index=[1, 2, 3, 4, 5, 7])
# print(df3.join(df4))
# print(df4.join(df3))

df5 = pd.DataFrame({
    'Name': ['Amit', 'Priya', 'Rahul']
})

df6 = pd.DataFrame({
    'Name': ['Sneha', 'Raj', 'Ammy']
}) 

# print(pd.concat([df5, df6], axis=0, ignore_index=True))
print(pd.concat([df5, df6], axis=1, ignore_index=True))
