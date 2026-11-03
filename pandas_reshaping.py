import pandas as pd

df = pd.DataFrame({
    "Name":["Amit", "Amit", "Pooja", "Pooja"],
    "Subject":['Math', 'Science', 'Math', 'Science'],
    "Marks":[80, 90, 78, 95]
})
# print(df.pivot(
#     index='Subject',
#     columns='Name',
#     values='Marks'
# ))

df1 = pd.DataFrame({
    'City': ['Pune', 'Pune', 'Mumbai', 'Mumbai'],
    'Product': ['Mobile', 'Mobile', 'Laptop', 'Laptop'],
    'Sales': [10000, 15000, 30000, 25000]
})
# print(df1.pivot_table(
#     index='City',
#     columns='Product',
#     values='Sales',
#     aggfunc='max'
# ))

df2 = pd.DataFrame({
    'Name': ['Amit', 'Priya'],
    'Math': [85, 95],
    'Science':[90, 80]
})
# print(df2)
# print(pd.melt(df2, id_vars=['Name'], var_name='Subject', value_name='Marks'))

df3 = pd.DataFrame({
    'Math': [85, 95, 78],
    'Science':[90, 80, 95],
    'Physics':[78, 30, 92]
}, index=['Amit', 'Priya', 'Jasmin'])
print(df3)
print('Columns into rows')
print(df3.stack())
print('Rows into columns')
print(df3.unstack())
