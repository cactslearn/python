import pandas as pd

# marks = pd.Series([80, 90, 78, 95, 88])
# marks[4] = 92
# print(marks)
# print(marks[1])
# marks = pd.Series(
#     [80, 90, 78, 95, 88],
#     index=["Rahul", "Priya", "Amit", "Pooja", "jasmin"]
# )
# marks["Pooja"] = 92
# print(marks)
# print(marks["Amit"])

data = {
    "Name":["Rahul", "Priya", "Amit", "Pooja", "jasmin"],
    "Age":[22, 21, 20, 19, 23],
    "Marks":[80, 90, 78, 95, 88]
}
df = pd.DataFrame(data)
# print(df)
# print(df["Marks"])
# print(df.iloc[1])
# print(df.head(2))
# print(df.tail(2))
# print(df.info())
# print(df.describe())
# print(df.shape)
# print(df.columns)
print(df.dtypes)