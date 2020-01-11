# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:44:50 2020

@author: carin
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

import plotly.graph_objects as go
from plotly.offline import plot


fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()

fig = go.Figure(data=[{'type': 'scatter','x':[1.5,2.1,2.2],'y': [2, 1, 4]}])
plot(fig)

url = 'http://bit.ly/kaggletrain'
train = pd.read_csv(url)
train.head()



X = train.iloc[1:,7].value.reshape(-1,1) 
#select 7th column from dataset, convert values, and reshape -1 means auto calculate shape of rows (e.g matrix multiplication?), all should have value of 1
Y = train.iloc[1:,11].value.reshape(-1,1)
lr = LinearRegression()
lr.fit(X,Y)
Y_pred = lr.predict(X)






