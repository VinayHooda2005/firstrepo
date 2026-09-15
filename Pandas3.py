import pandas as pd
df =pd.read_csv("data.csv")

#  to find which row is duplicate

print(df.duplicated())

# to remove the row which is dulplicate

df.drop_duplicates(inplace=True)
print(df.to_string())