
import pandas as pd
import numpy as np

data ={
    'Transaction_ID' :[1001,1002,1003,1004,1005,1006],
'Customer_Name':["Ahmed Ali","Sara Omar","Ali Saleh","Nada Hassan","Omar Khalid","Ahmed Ali"],
'Age':[28 , np.nan,35,42,np.nan,28],
'Email':["ahmed@mail.com","sarah@mail.com",np.nan, "nada@mail.com","omar@mail.com","ahmed@mail.com"],
'Join_Data':['2025-01-10','2025-02-15','2025-03-20',np.nan,'2025-05-05','2025-01-10'],
'Total_Purchase':[250,300,150,400,np.nan,250]
}
df=pd.DataFrame(data)
df
print(df)
print("*****************************")
df['Join_Data']=pd.to_datetime(df['Join_Data'])
print(df.dtypes)
print("*****************************")

var = df[df.isnull().sum(axis=1) >1]
print(var)
print("*****************************")

df.info()
print("*****************************")

print (df.isnull().sum())
print("*****************************")

var2 = df[df['Age']>30]
print (var2)
print("*****************************")

var3 = df.dropna()
print(var3)
print("*****************************")

df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df)
print("*****************************")

df['Total_Purchase'].fillna(0,inplace=True)
print(df)
print("*****************************")

df.drop_duplicates(inplace=True)
print(df)
print("*****************************")


print(df[df.duplicated()])

