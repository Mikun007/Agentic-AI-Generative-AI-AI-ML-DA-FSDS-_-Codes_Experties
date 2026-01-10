# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 09:23:04 2026

@author: mikun
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv(r"C:\Users\mikun\Downloads\Churn_Modelling.csv")
X = dataset.iloc[:, 3:-1]
y = dataset.iloc[:, -1]


# Encoding categorical data
# Label Encoding the "Gender" column
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X.iloc[:, 2] = le.fit_transform(X.iloc[:, 2])


# One Host Encoding the "Geography" column
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(
    transformers=[
        ("encoder", OneHotEncoder(), [1])
    ],
    remainder="passthrough")
X= np.array(ct.fit_transform(X))
print(X)

# Splitting the dataset into the Trainning set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=0)


from xgboost import XGBClassifier
classifier = XGBClassifier(random_state=0)
classifier.fit(X_train, y_train)

# prediction
y_pred = classifier.predict(X_test)

# Makng the confusino matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac)

bias = classifier.score(X_train, y_train)
print(bias)

variance = classifier.score(X_test, y_test)
print(variance)