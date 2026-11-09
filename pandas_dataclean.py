import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Jasmin', None],
    'Age': [22, np.nan, 25, np.nan, 28, np.nan],
    'Salary': [25000, 40000, np.nan, 50000, 35000, np.nan],
    'City': ['Pune', 'Mumbai', None, 'Pune', 'Chennai', None]
}

df = pd.DataFrame(data)
# print(df)

# Identification Of Missing Values
# print(df.isnull())
# print(df.isna())
# print(df.isna().sum())
# print(df.isna().sum().sum())
# print(df[df.isnull().any(axis=1)])
# print(df.isnull().any())
# print(df.isnull().any(axis=1))
# print(df[df.notnull().all(axis=1)])

# Dropping rows columns having missing values
# print(df.dropna())
# print(df.dropna(axis=1))
# print(df.dropna(how='all'))
# print(df.dropna(subset=['Age', 'Salary']))

# Filling value
# print(df.fillna(0))
# df['Age'] = df['Age'].fillna(df['Age'].mean())
# df['Salary'] = df['Salary'].fillna(df['Salary'].median())
# df['City'] = df['City'].fillna(df['City'].mode()[0])
# print(df)

mean_imputer = SimpleImputer(strategy='mean')
df[['Age', 'Salary']] = mean_imputer.fit_transform(df[['Age', 'Salary']])
print(df)

