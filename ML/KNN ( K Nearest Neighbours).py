# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 09:45:31 2026

@author: mikun
"""

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
# Feature scalling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Training the KNN model ont he training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

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


