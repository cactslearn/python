import pandas as pd

data = {
    "Name":["Rahul", "Priya", "Amit", "Pooja", "Jasmin"],
    "Age":[22, 21, 20, 19, 23],
    "Marks":[80, 90, 78, 95, 88]
}

df = pd.DataFrame(data, index=["A", "B", "C", "D", "E"])
# print(df)
# print(df.loc["A"])
# print(df.iloc[0])
# print(df.loc[["A", "C"]])
# print(df.iloc[[0, 3]])
# print(df.loc["A", "Name"])
# print(df.iloc[0, 0])
# print(df.loc["A":"C"])
# print(df.iloc[0:3])
# print(df.loc[:,"Name"])
# print(df.iloc[:,0])
# print(df.loc[:,["Name","Marks"]])
# print(df.iloc[:,[0, 2]])
# print(df.loc[:,"Name":"Marks"])
# print(df.iloc[:,0:3])

# print(df[df["Age"] > 20])
# print(df[(df["Age"] > 20) & (df["Marks"] > 80)])
print(df[(df["Age"] > 25) | (df["Marks"] > 90)])