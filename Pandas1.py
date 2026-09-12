# DataFrames in pandas 

import pandas as pd
data={
    'Name':['Rahul','Riya','Priya'],
    'Age':[22,19,23]
    }
df=pd.DataFrame(data,index=['a','b','c'])
print(df)
print("==================")

print(df.loc['a'])
print(df.iloc[2])
print("===========================")

# add new column
df['Job']=['IT','N/A','Sales']
print(df)
print("==========================")

# adding a new row 
new_row=pd.DataFrame([{'Name':'Anisha','Age':24,'Job':'HR'},{'Name':'Sandy','Age':25,'Job':'Engineer'}],index=['d','e'])
df=pd.concat([df,new_row])
print(df)
print("==================")

data={
    'Subject':['Math','Science','English'],
    'Marks':[85,90,78]
}
df=pd.DataFrame(data,index=['S1','S2','S3'])
print(df)
print(df.loc['S2'])
print("=================")

df['Grade']=['B','A','C']
print(df)
print("==========================")

new_row=pd.DataFrame([{'Subject':'History','Marks':88,'Grade':'A'}],index=['S4'])
df=pd.concat([df,new_row])
print(df)