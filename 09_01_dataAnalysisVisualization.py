# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:55:30 2020

@author: carin
"""

'''This file is for data analysis and data visualisation'''
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
import plotly.express as px
import plotly as py
import plotly.graph_objs as go
from scipy import special

fig = go.Figure(data=go.Bar(x=[1,5,8],y=[1, 1, 1]))
fig.write_html('blabl.html',auto_open=True)

df = px.data.tips()
fig2 = px.pie(df, values='tip', names='day')
fig2.write_html('first_figure.html', auto_open=True)

'''
x = np.linspace(0,np.pi,1000)

layout = go.Layout(titel='Example',yaxis=dict(title='volts'),xaxis=dict(title='nanoseconds'))

trace1 = go.Scatter(x=x,y=np.sin(x),mode='lines',name='sin(x)',line=dict(shape='spline'))

fig = go.Figure(dat=[trace1], layout=layout)
py.iplot(fig)'''