import pandas as pd


data = {'Name': ['John', 'Anna', None, 'Linda'],
        'Age': [28, None, 35, 32],
        'Country': ['USA', 'UK', 'Australia', None]}
df = pd.DataFrame(data)

print(df.isnull().sum())

df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'Country': 'Unknown'}, inplace=True)

print(df)