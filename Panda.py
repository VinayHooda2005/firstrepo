# Series in pandas

import pandas as pd 
data=[100,200,300]
series=pd.Series(data)
print(series.to_string(index=False))
print("=========================")


data=[100,200,300]
series=pd.Series(data,index=['a','b','c'])
print(series.loc['c'])  # loc use for index label value
print(series.iloc[0])   # iloc use for index value
print("==========================")


data=[1000.2,200.5,120.8]
series=pd.Series(data)
print(series)
print("====================")


data=[100,200,300]
series=pd.Series(data,index=['a','b','c'])
series.iloc[2]=500
print(series)

data=[100,200,300]
series=pd.Series(data,index=['a','b','c'])
series.loc['b']=500
print(series)

data=[100,200,300]
series=pd.Series(data,index=['a','b','c'])
series.iloc[2]+=500
print(series)
print("================")

data=[12,34,54,32,27,65]
series=pd.Series(data)
print(series[series>=35])
print("=======================")


calories={
    'Day 1':1720,
    'Day 2':2000,
    'Day 3':1800
}
series=pd.Series(calories)
print(series)

calories={
    'Day 1':1720,
    'Day 2':2000,
    'Day 3':1800
}

series=pd.Series(calories)
series.loc['Day 1']=1900
print(series)