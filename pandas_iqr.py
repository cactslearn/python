import pandas as pd

data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 25, 100]

df = pd.DataFrame({'Salary':data})
# print(df)
q1 = df['Salary'].quantile(0.25)
q3 = df['Salary'].quantile(0.75)
print('Quantile:', q1, q3)

iqr = q3 - q1
print('IQR: ', iqr)

lower_bond = q1 - 1.5 * iqr
higher_bond = q3 + 1.5 * iqr
print('Boundry: ', lower_bond, higher_bond)

df['Outlier']= (
    (df['Salary'] < lower_bond) | (df['Salary'] > higher_bond)
)
print(df[df['Outlier']])



