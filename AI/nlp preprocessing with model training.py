# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 09:42:19 2026

@author: mikun
"""

# Importing dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv(r"C:\Users\mikun\Downloads\Restaurant_Reviews.tsv", delimiter='\t', quoting=3)

# Cleaning the textts
import re # regular expression
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# corpus data
corpus = []


for i in range(0, len(dataset)):
    review = re.sub("[^a-zA-Z]", " ", dataset["Review"][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in stopwords.words("english")]
    review= " ".join(review)
    corpus.append(review)
    

# Creating the BAg of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Splitting the dataset into the training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)


from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Predicting the test set result
y_pred = classifier.predict(X_test)


from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
cm_dt = confusion_matrix(y_test, y_pred)
cr_dt = classification_report(y_test, y_pred)

training_acc = accuracy_score(y_train, classifier.predict(X_train))
ac_dt = accuracy_score(y_test, y_pred)

# random forest 
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)

cm_rf = confusion_matrix(y_test, y_pred_rf)
ac_rf = accuracy_score(y_test, y_pred_rf)
cr_rf = classification_report(y_test, y_pred)


training_acc_rf = accuracy_score(y_train, rf.predict(X_train)) # bias
test_acc_rf = accuracy_score(y_test, y_pred_rf) # variance

# KNN 
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

y_pred_knn = knn.predict(X_test)

cm_knn = confusion_matrix(y_test, y_pred_knn)
cr_knn = classification_report(y_test, y_pred_knn)

training_acc_knn = accuracy_score(y_train, knn.predict(X_train)) #bias
test_acc_knn = accuracy_score(y_test, y_pred_knn) #variance
# The KNN is High Bias

# Naiv Bays MultinomialNB
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB
nb_mul = MultinomialNB()
nb_mul.fit(X_train, y_train)

y_pred_nb = nb_mul.predict(X_test)

cm_nb = confusion_matrix(y_test, y_pred_nb)
cr_nb = classification_report(y_test, y_pred_nb)

training_acc_nb = accuracy_score(y_train, nb_mul.predict(X_train))
test_acc_nb = accuracy_score(y_test, y_pred_nb)
# 2nd Best fitted model Naive Bays MultinomialNB
# bias = 0.945
# virance = 0.74


# Naive Bays BernoulliNB
nb_ber = BernoulliNB()
nb_ber.fit(X_train, y_train)

y_pred_ber = nb_ber.predict(X_test)

cm_ber = confusion_matrix(y_test, y_pred_ber)
cr_ber = classification_report(y_test, y_pred_ber)

training_acc_ber = accuracy_score(y_train, nb_ber.predict(X_train))
test_acc_ber = accuracy_score(y_test, y_pred_ber)
#Best fitted model Naive Bays BernoulliNB
# bias = 0.94625
# variance = 0.745


# Naive Bays GaussianNB
nb_ga = GaussianNB()
nb_ga.fit(X_train, y_train)

y_pred_ga = nb_ga.predict(X_test)

cm_ga = confusion_matrix(y_test, y_pred_ga)
cr_ga = classification_report(y_test, y_pred_ga)

training_acc_ga = accuracy_score(y_train, nb_ga.predict(X_train))
test_acc_ga = accuracy_score(y_test, y_pred_ga)


# TF-IDF with BernoulliNB and hyperparameter tuning
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1,2)
    )
X = tfidf.fit_transform(corpus).toarray()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

nb_ber = BernoulliNB()
nb_ber.fit(X_train, y_train)

y_pred_ber = nb_ber.predict(X_test)

cm_ber = confusion_matrix(y_test, y_pred_ber)
cr_ber = classification_report(y_test, y_pred_ber)

training_acc_ber = accuracy_score(y_train, nb_ber.predict(X_train))
test_acc_ber = accuracy_score(y_test, y_pred_ber)



























