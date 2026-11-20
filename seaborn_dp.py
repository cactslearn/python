import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'age':[20, 25, 30, 35, 40],
    'salaries':[10000, 15000, 20000, 30000, 40000]
    # 'marks':[100, 80, 60, 40, 20]
    # 'marks':[20, 20, 20, 20, 20]
})

# sns.histplot(df, x='age', y='salaries')
# sns.kdeplot(df, x='age')
# sns.displot(data=df, x='age', kind='hist')
# sns.displot(data=df, x='age', kind='kde')
sns.pairplot(df)
plt.show()