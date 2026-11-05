import pandas as pd

df = pd.DataFrame({
    'Employee_Id': [101, 102, 103, 104, 105],
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Raj'],
    'Department': ['IT', 'HR', 'IT', 'HR', 'IT'],
    'Salary': [25000, 40000, 50000, 35000, 30000]
})
# print(df)
df.to_parquet('employees.parquet', engine='pyarrow', compression="gzip", index=False)
print(pd.read_parquet('employees.parquet', engine='pyarrow'))
# print(pd.read_parquet('employees.parquet', engine='pyarrow', columns=['Name', 'Salary']))

# df = pd.read_parquet('employees.parquet', engine='pyarrow')
# filter_df = df[df['Salary'] > 35000]
# print(filter_df)

