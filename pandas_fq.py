import pandas as pd
data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha'],
    'Age': [22, 25, 30, 28],
    'Salary': [25000, 40000, 50000, 35000]
}

df = pd.DataFrame(data)
# print(df[df['Age'] > 25])
# print(df[(df['Age'] > 25) & (df['Salary'] > 40000)])
# print(df[(df['Age'] > 25) | (df['Salary'] > 40000)])

# print(df.query('Age > 25'))
# print(df.query('Age > 25 and Salary > 40000'))
# print(df.query('Age > 25 or Salary > 40000'))

print(df[df['Name'].isin(['Amit', 'Rahul', 'Sneha'])])