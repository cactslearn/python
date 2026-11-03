import polars as pl
# import pandas as pd

# pandas_df = pd.DataFrame({
#     'Name': ['Amit', 'Priya', 'Rahul', 'Sneha'],
#     'Age': [22, 25, 30, 28],
#     'Salary': [25000, 40000, 50000, 35000]
# })
# print(pandas_df)

polars_df = pl.DataFrame({
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha'],
    'Age': [22, None, 30, 28],
    'Salary': [25000, 40000, 50000, 35000]
})
# print(polars_df)
# print(polars_df.select(["Name", "Salary"]))
# print(polars_df.filter(
#     pl.col("Salary") > 30000
# ))
# print(polars_df.with_columns(
#     (pl.col("Salary") * 12).alias("Annual_Salary")
# ))

df = pl.DataFrame({
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Raj'],
    'Department': ['IT', 'HR', 'IT', 'HR', 'IT'],
    'Salary': [25000, 40000, 50000, 35000, 30000]
})
# print(df.group_by("Department").agg(
#     pl.col("Salary").mean().alias("Average_Salary")
# ))
# print(df.sort("Salary", descending= True))

# print(polars_df.with_columns(
#     pl.col("Age").fill_null(0)
# ))

print(
    polars_df.lazy()
    .filter(pl.col("Salary") > 30000)
    .select(["Name", "Salary"])
    .collect()
)