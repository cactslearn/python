import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "hours": [ 1.5, 2.0, 3.0, 4.5, 5.0, 6.5, 2.5, 3.5, 4.0, 5.5, 6.0, 7.0],
    "score":[55, 60, 68, 76, 80, 91, 58, 66, 72, 82, 86, 94],
    "track":[
        "STEM",  "STEM", "STEM", "STEM", "RIGHT", "RIGHT",
        "RIGHT", "RIGHT", "Humanities", "Humanities", "Humanities", "Humanities",
    ]
}

df = pd.DataFrame(data=data)

# sns.regplot(data=df, x="hours", y="score", ci=95)
# plt.title("Study Hours vs. Exam Score")
# plt.show()
# sns.regplot(data=df, x="hours", y="score", order=2, scatter_kws={"alpha":1})
# plt.title("Study Hours vs. Exam Score")
# plt.show()

g = sns.lmplot(data=df, x="hours", y="score", hue="track",col="track", height=4, aspect=1.1)
g.figure.suptitle("Regression by Track")
plt.show()