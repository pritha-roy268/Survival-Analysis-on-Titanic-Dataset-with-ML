# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:07:30 2020



import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("D:\python assignments\datasets\datasets_train.csv")
df.head()
'''
#No of passengers/Parch
figure = plt.figure(figsize=(25,7))
plt.hist([df[df['Survived']==1]['Parch'],df[df['Survived']==0]['Parch']],stacked=True, 
         color=['y','r'], bins=50,label=['Survived' , 'Dead'])
plt.xlabel('Parch')
plt.ylabel('Number Of Passengers')
plt.legend()

#No of passengers/SibSp
figure = plt.figure(figsize=(25,7))
plt.hist([df[df['Survived']==1]['SibSp'],df[df['Survived']==0]['SibSp']],stacked=True, 
         color=['g','r'], bins=50,label=['Survived' , 'Dead'])
plt.xlabel('SibSp')
plt.ylabel('Number Of Passengers')
plt.legend()


#Count/Sex
sns.catplot(x ="Sex", hue ="Survived",  
kind ="Count", data = df) '''

#No of passengers/Age
figure = plt.figure(figsize=(25,7))
plt.hist([df[df['Survived']==1]['Age'],df[df['Survived']==0]['Age']],stacked=True, 
         color=['b','r'], bins=50,label=['Survived' , 'Dead'])
plt.xlabel('Age')
plt.ylabel('Number Of Passengers')
plt.legend()
'''
#No of passengers/Pclass
figure = plt.figure(figsize=(25,7))
plt.hist([df[df['Survived']==1]['Pclass'],df[df['Survived']==0]['Pclass']],stacked=True, 
         color=['g','r'], bins=50,label=['Survived' , 'Dead'])
plt.xlabel('Pclass')
plt.ylabel('Number Of Passengers')
plt.legend()


#No of passengers/Pclass
total = df.isnull().sum().sort_values(ascending=False)
percent_1 = df.isnull().sum()/df.isnull().count()*100
percent_2 = (round(percent_1, 1)).sort_values(ascending=False)
missing_data = pd.concat([total, percent_2], axis=1, keys=['Total', '%'])
missing_data.head(5)
df.columns.values

plt.hist([df[df['Survived']==1]['Pclass'],df[df['Survived']==0]['Pclass']],stacked=True, 
         color=['g','r'], bins=25,label=['Survived' , 'Dead'])
plt.xlabel('Pclass')
plt.ylabel('Number Of Passengers')
plt.legend()

#Count vs. Survived,Sex,Pclass,SibSp,Parch,Embarked plots
cols = ['Survived','Sex', 'Pclass', 'SibSp', 'Parch', 'Embarked']

nr_rows = 2
nr_cols = 3

fig, axs = plt.subplots(nr_rows, nr_cols, figsize=(nr_cols*3.5,nr_rows*3))

for r in range(0,nr_rows):
    for c in range(0,nr_cols):  
        
        i = r*nr_cols+c       
        ax = axs[r][c]
        sns.countplot(df[cols[i]], hue=df["Survived"], ax=ax)
        ax.set_title(cols[i], fontsize=14, fontweight='bold')
        ax.legend(title="survived", loc='upper center') 
        
plt.tight_layout()'''












