# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 10:03:05 2026

@author: mikun
"""

# Naive Bayes

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"C:\Users\mikun\Downloads\logit classification.csv")

X = dataset.iloc[:, [2, 3]]
y = dataset.iloc[:, -1]


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=0
                                                    )

# without scalling
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

gs = GaussianNB()
gs.fit(X_train, y_train)

y_pred = gs.predict(X_test)

# Scoring

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac)

bias = gs.score(X_train, y_train)
print(bias)

variance = gs.score(X_test, y_test)
print(variance)















