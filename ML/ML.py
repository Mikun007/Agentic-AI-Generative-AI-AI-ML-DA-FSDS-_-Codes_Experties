import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv(r"C:\Users\mikun\Downloads\Data.csv")

# Splitting the x and y according to dependent and independent variable

# independent variable
x = dataset.iloc[:, :-1].values

# dependent variable
y = dataset.iloc[:, 3].values


# sklearn imputation techniques 
# sklearn.impute == transformer to fil missing value
# simpleimputer fit & transform
from sklearn.impute import SimpleImputer

# strategy = {'mean', 'median', 'most_frequent(mode)}
imputer = SimpleImputer(strategy="most_frequent")

imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])


# converting string to machine understandable code
# sklearn.preprocessing == scaling, binariation, normalization, cetring
# labelencoder == transformer to transform categorical to numerical
from sklearn.preprocessing import LabelEncoder

labelencoder_x = LabelEncoder()
# labelencoder_x.fit_transform(x[:, 0])
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])

# transforming y
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# splitting train and test data
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    train_size=0.8, # you can write this
                                                    test_size=0.2, # or you can write this
                                                    random_state=0
                                                    )














