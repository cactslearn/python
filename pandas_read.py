import pandas as pd
import sqlite3

# df = pd.read_csv("student.csv", skiprows=1, header=None)
# print(df)

# df = pd.read_excel("student.xlsx", sheet_name="student", skiprows=1, header=None)
# print(df)

# df = pd.read_json("student.json")
# print(df)

connection = sqlite3.connect("student.db")
df = pd.read_sql("select * from student", connection)
print(df)
connection.close()