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


dataset = load_boston()

X = dataset.data
y = dataset.target[:,np.newaxis]

print("Total samples in our dataset is: {}".format(X.shape[0]))



url = 'C:\Users\carin\Documents\Studium\Bachelor\6. Semester\Bachelorarbeit\E-Mobilität\Daten\Info\Ausschluss_Limesurvey_RICHTIG\Info_Limesurvey_Aussortiert(60,61,106) + CBC_ID + SurveyID'
bachelorDf = pd.read_csv(url)
print(bachelorDf)


'''fig = px.scatter(dataset, x="sepal_width", y="sepal_length")
fig.show()'''