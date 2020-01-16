#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
from sklearn.linear_model import LinearRegression

import plotly.graph_objects as go
from plotly.offline import plot
import plotly.express as px



df = pd.read_csv(r'C:\Users\carin\Documents\GitHub\DataAnalysisVisualization\Dataset_AnaVis.csv',sep=';',error_bad_lines=False)
df.head()
df=df.dropna(axis=1,how='all')
df.head()


fig = px.bar(df, x='Age', y='EnvironmentalAttitude')
fig.show()

fig = px.scatter(df, x="Age", y="EnvironmentalAttitude")
fig

fig = px.scatter(df, x="Age", y="EnvironmentalAttitude",marginal_y="rug", marginal_x="histogram")
fig

fig = px.scatter(df, x="Age", y="EnvironmentalAttitude",color="Sex",marginal_y="rug", marginal_x="histogram")
fig


X = df.iloc[:,7]
Y = df.iloc[:,11]
lr = LinearRegression()
lr.fit(X,Y)
Y_pred = lr.predict(X)


# In[ ]:





# In[ ]:




