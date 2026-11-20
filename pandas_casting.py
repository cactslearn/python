import pandas as pd

df = pd.DataFrame({
    'price': ['10.20', '20.00', 'invalid', '15.25'],
    'date': ['2026-11-16', '2026-11-17', '2026-18-11', '11-19-2026'],
    'rating': [1, 5, 3, 2]
})
print(df)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['date'] = pd.to_datetime(df['date'], format='%m-%d-%Y', errors='coerce')
df['rating'] = df['rating'].astype('category')
print(df.dtypes)
print(df)
