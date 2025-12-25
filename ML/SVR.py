# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 09:42:49 2025

@author: mikun
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import the dataset
dataset = pd.read_csv(r"C:\Users\mikun\Downloads\emp_sal.csv")
X = dataset.iloc[:, 1:2]
y = dataset.iloc[:, 2]

# Fitting SVR to the dataste
from sklearn.svm import SVR

regressor = SVR(kernel="poly", degree=4, gamma="auto", C=5.0)
regressor.fit(X, y)


y_pred_svr = regressor.predict([[6.5]])
print(y_pred_svr)


# KNN model predictions
from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(n_neighbors=4, weights="distance")
knn_reg.fit(X, y)

y_pred_knn = knn_reg.predict([[6.5]])
print(y_pred_knn)



