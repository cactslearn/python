import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = [45, 50, 55, 60, 65, 70, 75, 80, 200]
plt.boxplot(data)
plt.title('Box Plot')
plt.show()