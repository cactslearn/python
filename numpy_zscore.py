import numpy as np
from scipy.stats import zscore

marks = [30, 40, 50, 60, 70, 80, 90, 100]
print(marks)
mean = np.mean(marks)
print('Mean: ', mean)
std = np.std(marks)
print('STD: ',std)
z_scores = zscore(marks)
print('Z-Scores', z_scores)