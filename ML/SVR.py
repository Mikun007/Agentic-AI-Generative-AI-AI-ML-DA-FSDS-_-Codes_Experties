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
knn_reg = KNeighborsRegressor(n_neighbors=2, weights="distance", algorithm="brute")
knn_reg.fit(X, y)

y_pred_knn = knn_reg.predict([[6.5]])
print(y_pred_knn)

# Decission Tree
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor(criterion="poisson",
                               max_depth=3,
                               random_state=0
                               )
dt_reg.fit(X, y)

dt_pred = dt_reg.predict([[6.5]])
print(dt_pred)

# Random Forest Algorithm
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(random_state=43, n_estimators=20)
rf_reg.fit(X, y)

rf_pred = rf_reg.predict([[6.5]])
print(rf_pred)





























