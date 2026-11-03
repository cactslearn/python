import numpy as np
import io

raw_data = """name,math,science|Amit,85,90|Rahul,90,|Arti,95,92|Priya,80,85|Neha,,98"""
data = raw_data.replace('|','\n')

students = np.genfromtxt(
    io.StringIO(data),
    delimiter=',',
    names=True,
    dtype=[('name', 'U20'),('math', 'f8'), ('science', 'f8')],
    filling_values=0,
    encoding='utf8'
)
print(students)
print(students['math'])
print(students['science'])
totals = students['math'] + students['science']
print(totals)
index = np.argmax(totals)
print(index)
print(students['name'][index], f"{totals[index]:.1f}")


