import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder

df = pd.DataFrame({
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Jasmin'],
    'City': ['Pune', 'Mumbai', 'Mumbai', 'Bombay', 'Chennai'],
    'Education': ['Postgraduate', 'PHD', 'Postgraduate', 'Graduate', 'Graduate'],
    'Experience_Level':['Beginner', 'Intermediate', 'Advanced', 'Beginner', 'Intermediate']
});

# df['City_Encoded'] = LabelEncoder().fit_transform(df['City'])

# encoded_df = pd.get_dummies(df, columns=['Education'], dtype=int)
# print(encoded_df)

encoder = OrdinalEncoder(categories=[['Intermediate', 'Beginner', 'Advanced']])
df['Experience_Encoder'] = encoder.fit_transform(df[['Experience_Level']]).astype(int)
print(df)


