import pandas as pd
import re

df = pd.DataFrame({
    'text': [' A pp le Inc. ', 'banana split', 'CHERRY-456', 'date fruit']
})
df['cleaned'] = df['text'].str.strip()
df['lowercase'] = df['text'].str.lower()
df['uppercase'] = df['text'].str.upper()
print(df)

has_fruit = df['text'].str.contains('apple|banana|cherry',case=False, regex=True)
print(has_fruit)

df['replaced'] = df['text'].str.replace('fruit', 'palm', regex=False)
print(df)

split_df = df['cleaned'].str.split(' ', expand=True, n=1)
print(split_df)

extracted = df['text'].str.extract(r'([A-Z]+)-(\d+)')
print(extracted)