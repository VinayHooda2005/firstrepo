# Dropna to delete null values in a DataFrame
import pandas as pd
df=pd.read_csv("data.csv")
df.dropna(inplace=True)
print(df.to_string())


new_df=df.dropna()
print(new_df.to_string())
