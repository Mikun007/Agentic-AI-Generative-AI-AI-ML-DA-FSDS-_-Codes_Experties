# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 12:27:10 2025

@author: mikun
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import statsmodels.api as sm

dataset = pd.read_csv(r"C:\Users\mikun\Downloads\Investment.csv")

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 4]

# Convert categorical values to binary
X = pd.get_dummies(X, dtype=int)

# Spliting the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=0)
# fitting the model with X_train and y_train
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting y from X_test
y_pred = model.predict(X_test)

# slop or coefficient
m = model.coef_
print(m)

# intercept or constant
c = model.intercept_
print(c)

# Better way to add column is 
X = sm.add_constant(X)


X_opt = X.copy()
SL = 0.05
removed = []

while True:
    regressor = sm.OLS(endog=y, exog=X_opt).fit()
    p_values = regressor.pvalues.drop("const")
    
    if p_values.max() > SL:
        worst_feature = p_values.idxmax()
        removed.append(worst_feature)
        X_opt = X_opt.drop(columns=worst_feature)
    else:
        break
    

print("Removed features (order):", removed)
print("Final features:", X_opt.columns.tolist())

import pickle
filename = "profit_prediction.pkl"
with open(filename, "wb") as file:
    pickle.dump(model, file)
    
pickle.dump(X_train.columns.tolist(), open("profit_pred_cols.pkl", "wb"))









