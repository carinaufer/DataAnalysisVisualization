# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:37:26 2020

@author: carin
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

import plotly.graph_objects as go
import plotly.express as px


#import csv file
df = pd.read_csv(r'C:\Users\carin\Documents\GitHub\DataAnalysisVisualization\Dataset_AnaVis.csv',delimiter=';', decimal=',',engine='python')
df.head() #show first 6 lines
dataTypeSeries = df.dtypes #variable for datytpyes
print(dataTypeSeries) #show datatypes
df.dropna(inplace = True) #drop rows with missing values in the set direct
df.head()

#cast to correct datatype
df['Sex'] = df['Sex'].astype('Int64')
df['Group'] = df['Group'].astype('Int64')
df['Age'] = df['Age'].astype('Int64')
df['RelativeAdvantage'] = df['RelativeAdvantage'].astype('Float64')
df['Complexity'] = df['Complexity'].astype('Float64')
df['Compatibility'] = df['Compatibility'].astype('Float64')
df['Attitude'] = df['Attitude'].astype('Float64')
df['SubjectiveNormPeers'] = df['SubjectiveNormPeers'].astype('Float64')
df['SubjectiveNormSociety'] = df['SubjectiveNormSociety'].astype('Float64')
df['SubjectiveNormMedia'] = df['SubjectiveNormMedia'].astype('Float64')
df['SubjectiveNormTotal'] = df['SubjectiveNormTotal'].astype('Float64')
df['PerceivedMoralNorm'] = df['PerceivedMoralNorm'].astype('Float64')
df['EnvironmentalAttitude'] = df['EnvironmentalAttitude'].astype('Float64')
df['SelfEfficacy'] = df['SelfEfficacy'].astype('Float64')
df['PurchaseInterest'] = df['PurchaseInterest'].astype('Float64')
df['EVChoice'] = df['EVChoice'].astype('Int64')
dataTypeSeries = df.dtypes #check result
print(dataTypeSeries)

# Code aus dem Youtube Video https://www.youtube.com/watch?v=X3ek_HIkZcQ, man bekommt aber einen Error, wegen unten beschriebenen Dimensions-Problem
print(df.iloc[:,7])
print(df.iloc[1:,7])
print(df.iloc[1:,7].value.reshape(-1,1))


#print plot with plotly express
fig = px.scatter(df, x="EnvironmentalAttitude", y="EVChoice", color="Sex", marginal_y="violin",marginal_x="box")
fig.show()

fig2 = px.scatter(df, x="EnvironmentalAttitude", y="EVChoice", color="Attitude", facet_col="Sex",color_continuous_scale=px.colors.sequential.Viridis, render_mode="webgl")
fig2.show()
'''
Wir haben vom CSV Dokument jetzt ein Panda-Dataframe (mit Header / Column Überschriften). Für die meisten Rechnungen brauchen wir aber ein NumpyArray, das unterscheidet sich irgendwie von den Dimensionen (1 versus 2-dimensional).
@Thoma kannst du dir das vlt irgendwie angucken bis morgen?


https://medium.com/dunder-data/from-pandas-to-scikit-learn-a-new-exciting-workflow-e88e2271ef62
Most Scikit-Learn estimators require that data be strictly 2-dimensional. 
If we select the column above as train['HouseStyle'], technically, a Pandas Series is created which is a single dimension of data. 
We can force Pandas to create a one-column DataFrame, by passing a single-item list to the brackets like this:
    df_01 = df[['column']].copy()
>>> df_01.ndim
2'''

                 
