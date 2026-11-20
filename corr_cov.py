import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'hours':[1, 2, 3, 4, 5],
    # 'marks':[20, 40, 60, 80, 100]
    # 'marks':[100, 80, 60, 40, 20]
    'marks':[20, 20, 20, 20, 20]
})
# print(df['hours'].corr(df['marks']))
# print(df['hours'].cov(df['marks']))

# print(df.corr())
# sb.heatmap(df.corr(), annot= True)
# plt.title('Correlation Heatmap')
# plt.show()

sb.heatmap(df.cov(), annot= True)
plt.title('Covarriance Heatmap')
plt.show()