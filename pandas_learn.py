import pandas as pd 
import numpy as np 

df = pd.read_csv("/home/shadowrc/Downloads/tested.csv")

# print(df.head())
# print(df.shape)
# df.info()
# print(df.describe())
# print(df.isnull())

# print(df.tail(3))
# print(df.shape)
# print(df.dtypes)

# print(df['Age'])

# print(df[['Age','Name','Survived']])

# print(  df [   (df ['Survived'] == 1) & (df['Age'] < 15)  ]     [['Age','Name']]   )

# print(df[df['Pclass'] == 1].head(10))


# cleaning data

# print("total missing values are : \n" ,df.isnull().sum())

# df['Age'] = df['Age'].fillna(df['Age'].median())

# print("total missing values are :",df['Age'].isnull().sum())

# df = df.drop(columns=['Cabin','Ticket'])

# df = df.dropna()

# print(df.isnull().sum())

# print(df['Pclass'].head())

# print(df['Survived'].mean())

# print(df.groupby('Pclass')['Age'].mean())

# print(df['Age'].value_counts())

# print(df.groupby('Sex')['Survived'].sum())

# print(df.groupby('Sex')['Survived'].mean())

print(df['Pclass'].value_counts())

print(df.columns)

print(df.groupby('Survived')['Fare'].mean())

print(df['Age']>60)

print(df [df ['Age'] > 60 ]  [['Name','Age','Survived']] )

print(df.groupby('Pclass')['Survived'].mean()*100)

df['AgeGroup'] = np.where(df['Age']<18 , 'Child','Adult')

print(df['AgeGroup'].head(10))

print( df[(df['AgeGroup']=='Child') & (df['Survived']==1)] [['Name','Age']].head(10)  )

print( df[(df['AgeGroup']=='Child') & (df['Survived']==1)].shape[0]  )


# print("max Fare paid : " ,df['Fare'].max())

# print(df[df['Fare']==df['Fare'].max()] [['Name','Age','Fare']])
