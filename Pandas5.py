# Use of fillna in Pandas to fill missing values in a DataFrame 


import pandas as pd
df=pd.read_csv("data.csv")
df.fillna(123, inplace=True)
print(df.to_string())

import pandas as pd

df = pd.read_csv('data.csv')

numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(130)

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Date'] = df['Date'].fillna(pd.Timestamp('1970-01-01'))

print(df.to_string())
