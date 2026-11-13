import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range('2026-11-10', periods=7),
    'Temperature': [np.nan, 25, np.nan, 38, np.nan, np.nan, np.nan]
}

df = pd.DataFrame(data)
df['Temperature'] = df['Temperature'].ffill()
# df['Temperature'] = df['Temperature'].bfill()
print(df)
