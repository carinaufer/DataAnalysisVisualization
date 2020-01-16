import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


#import csv file
pth = input('Please enter the path of the CSV file')
df = pd.read_csv(pth, delimiter=';', decimal=',',engine='python')
df.head() #show first 6 lines
dataTypeSeries = df.dtypes #variable for datytpyes
#print(dataTypeSeries) #show datatypes
df.dropna(inplace = True) #drop rows with missing values in the set direct
df.head()
npdf = df.to_numpy(copy=True)

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
#print(dataTypeSeries)

x = npdf[:,2].reshape(-1, 1)
y = npdf[:,3].reshape(-1, 1)
#print(x)
#print('______________')
#print(y)
lr = LinearRegression()
lr.fit(x,y)
y_pred = lr.predict(x)
plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
plt.show()

#print plot with plotly express
fig = px.scatter(df, x="EnvironmentalAttitude", y="EVChoice", color="Sex", marginal_y="violin",marginal_x="box")
fig.show()

fig2 = px.scatter(df, x="EnvironmentalAttitude", y="EVChoice", color="Attitude", facet_col="Sex",color_continuous_scale=px.colors.sequential.Viridis, render_mode="webgl")
fig2.show()