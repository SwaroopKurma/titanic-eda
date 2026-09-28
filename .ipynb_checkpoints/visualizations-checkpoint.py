import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


df = pd.read_csv("/home/shadowrc/Downloads/tested.csv")

print(df.shape)

df['Age'] = df['Age'].fillna(df['Age'].median())
df['AgeGroup'] = np.where(df['Age']<18,'Child','Adult')

print(df.shape)
print(df.head())
print(df)