import pandas as pd
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 10, 40, 10]
plt.plot(x, y, linestyle ="-.", color="red", label="Test Label")
plt.legend()
plt.title('Line Plot', fontsize=20)
plt.xlabel('X-axis', fontsize =20)
plt.ylabel('Y-lable', fontsize = 20)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)

plt.savefig("linechart.pdf", dpi=300)
plt.show()

# categories = ['A', 'B', 'C', 'D']
# values = [20, 35, 30, 45]
# plt.barh(categories, values)
# plt.title('Bar Chart')
# plt.show()

# x = [5, 10, 15, 20, 25]
# y = [10, 15, 12, 25, 30]
# plt.scatter(x, y)
# plt.title('Scatter Chart')
# plt.show()

# marks = [45, 50, 55, 60, 65, 70, 70, 75, 80, 85]
# plt.hist(marks, bins=5, color='green')
# plt.title('Histogram')
# plt.xlabel('Marks')
# plt.ylabel('Frequency')
# plt.show()

# data = [45, 50, 55, 60, 65, 70, 75, 80, 200]
# plt.boxplot(data)
# plt.title('Box Plot')
# plt.show()

# labels = ['A', 'B', 'C', 'D']
# sizes = [30, 25, 20, 25]
# plt.pie(sizes, labels=labels)
# plt.title('Pie Chart')
# plt.show()

# x = [1, 2, 3, 4, 5]
# y1 = [2, 3, 4, 5, 6]
# y2 = [1, 2, 3, 4, 5]

# plt.stackplot(x, y1, y2, labels=['A', 'B'], colors=['red', 'green'])
# plt.legend()
# plt.title('Area Plot')
# plt.show()