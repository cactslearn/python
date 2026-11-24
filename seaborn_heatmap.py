import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.DataFrame({
    "study_hours": [2, 4, 6, 8, 10],
    "sleep_hours": [8, 7, 7, 6, 5],
    "practice_tests":[1, 2, 4, 5, 7],
    "exam_score":[55, 64, 75, 84, 92]
})

# corr = df.corr()
# plt.figure(figsize=(6, 4))
# sns.heatmap(corr, annot= True, fmt=".2f", cmap="coolwarm", vmin= -1, vmax=1)
# plt.title("Feature Correlation Matrix")
# plt.tight_layout()
# plt.show()

sales = pd.DataFrame({
    "region":["North", "North", "South", "South", "East", "East", "West", "West"],
    "category":["Books", "Games", "Books", "Games", "Books", "Games", "Books", "Games"],
    "revenue":[1200, 2400, 950, 1800, 1500, 1100, 1750, 2900]
})
# pivot = sales.pivot(index="category", columns="region", values="revenue")

# plt.figure(figsize=(5, 4))
# sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu", linewidths=1, linecolor="white")
# plt.title("Revenue by Region and Category")
# plt.tight_layout()
# plt.show()

mduc = pd.DataFrame({
    "a":[10, 20, 30, 40],
    "b":[12, 19, 33, 38],
    "c":[40, 30, 18, 10],
    "d":[5, 15, 25, 35]
})

# corr = mduc.corr()
# mask = np.triu(np.ones_like(corr, dtype=bool),k=0)
# plt.figure(figsize=(5, 4))
# sns.heatmap(corr, mask=mask, annot= True, fmt=".2f", cmap="vlag", vmin= -1, vmax=1)
# # sns.heatmap(corr, annot= True, fmt=".2f", cmap="vlag", vmin= -1, vmax=1)
# plt.title("Lower-Triangle Correlation Heatmap")
# plt.tight_layout()
# plt.show()

custom = pd.DataFrame({
    "ad_spend": [12, 25, 40, 18, 35, 50, 22, 45],
    "conversion":[140, 290, 480, 195, 390, 610, 230, 520],
    "channel":["Search", "Search", "Search", "Social", "Social", "Social", "Email", "Email"],
    "region":["West", "East", "North", "South", "East", "West", "North", "South"],
    "reach_k":[30, 55, 90, 45, 80, 120, 40, 85]
})

plt.figure(figsize=(7, 4.5))
sns.scatterplot(data=custom, x="ad_spend", y="reach_k", 
                hue="channel", size="conversion", style="region",
                palette="Set2", sizes=(60, 260), alpha=0.85)
plt.tight_layout()
plt.show()