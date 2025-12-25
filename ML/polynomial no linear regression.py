# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 09:35:53 2025

@author: mikun
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# model imports
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv(r"C:\Users\mikun\Downloads\emp_sal.csv")
dataset

# deviding the independent and dependent varaible
X = dataset.iloc[:, 1:2]
y = dataset.iloc[:, 2]

lin_reg = LinearRegression()
lin_reg.fit(X, y)


# Linear regression visualization
plt.scatter(X, y, color="red")
plt.plot(X, lin_reg.predict(X), color="blue")
plt.title("Linear Regression graph")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()

lin_model_pred = lin_reg.predict([[6.5]])
print(lin_model_pred)

# we will be using polynomial model
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=6)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)


lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


# linear regression visualization

plt.scatter(X, y, color="red")
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color="blue")
plt.title("Truth or Bluff (Polynomial Regression)")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()


line_model_pred = lin_reg.predict([[6.5]])
lin_model_pred

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred













