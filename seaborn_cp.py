import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "department":[
        "Engineering", "Engineering", "Engineering", "Engineering", "Engineering", "Engineering",
        "Marketing", "Marketing", "Marketing", "Marketing", "Marketing", "Marketing",
        "Sales", "Sales", "Sales", "Sales", "Sales", "Sales",
    ],
    "level":[
        "Junior", "Junior", "Mid", "Mid", "Senior", "Senior",
        "Junior", "Junior", "Mid", "Mid", "Senior", "Senior",
        "Junior", "Junior", "Mid", "Mid", "Senior", "Senior",
    ],
    "salary_k":[
        72, 78, 105, 112, 142, 155,
        58, 63, 84, 90, 115, 124,
        62, 68, 92, 108, 130, 148
    ]
}

df = pd.DataFrame(data=data)

# sns.boxplot(data=df, x="level", y="salary_k", hue="department")
# plt.title("Salary Distribution by Department and Level")
# plt.show()

# sns.violinplot(data=df, x="level", y="salary_k", inner="quartile")
# plt.title("Salary Density by Department")
# plt.show()

# sns.barplot(data=df, x="level", y="salary_k", hue="department", errorbar="sd")
# plt.title("Average Salary by Department and Level")
# plt.show()

# sns.stripplot(data=df, x="level", y="salary_k", hue="department", jitter=True, dodge=True)
# plt.title("Individual Salary Observations")
# plt.show()

sns.countplot(data=df, x="department", hue="level")
plt.title("Headcount by Department and Level")
plt.show()