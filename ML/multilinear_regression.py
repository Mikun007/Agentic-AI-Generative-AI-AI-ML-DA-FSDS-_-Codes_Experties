# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 09:56:45 2025

@author: mikun
"""

# RFE (Recursive feature elimination)

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

# created new constant column
X = np.append(arr=np.full((50, 1), 1).astype(int), values=X, axis=1)
# Better way to add column is 
# X = sm.add_constant(X)

# Recursive backword elemenation
# endog = endogenous variable
# exog = exogenous variables
# sm.OLS() = create a Ordinary Least Sequence regresson model
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
# OrdinaryLeastSquares
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

# Eleminate x4 as it has p-value = 0.99
X_opt = X[:, [0, 1, 2, 3, 5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

# Eliminate x4 which was x5 in previous as it has p-value = 0.943
X_opt = X[:, [0, 1, 2, 3]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

# Eliminate X2 
X_opt = X[:, [0, 1, 3]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

# Eliminate X2 which was x3 in previous
X_opt = X[:, [0, 1]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

# bias
bias = model.score(X_train, y_train)
bias

# variance
variance = model.score(X_test, y_test)
variance


















