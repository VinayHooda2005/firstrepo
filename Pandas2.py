import pandas as pd
df=pd.read_csv("pokemon_list.csv")
print(df.to_string())

print(df[["NAME","WEIGHT (KG)"]].to_string())
print("===================")

print(df.loc[5])
print("===================")

df=pd.read_csv("pokemon_list.csv",index_col='NAME')
print(df.loc['Pikachu'])

print(df.iloc[10:20])
print("==========================")
