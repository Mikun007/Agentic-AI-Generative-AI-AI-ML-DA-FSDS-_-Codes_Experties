import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from scipy.stats import variation
from scipy.stats import stats
import pickle

# dataset import
dataset = pd.read_csv(r"C:\Users\mikun\Downloads\Salary_Data.csv")

# devide x and y
x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# train test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# model selection
regressor = LinearRegression()
# model fitting
regressor.fit(x_train, y_train)


# prediction using x_test
y_pred = regressor.predict(x_test)

# visualize the test set
plt.scatter(x_test, y_test, color="red")
plt.plot(x_train, regressor.predict(x_train), color="blue")
plt.title("Salary vs Experience (Test set)")
plt.xlabel("Year Of Experience")
plt.ylabel("Salary")
plt.show()

# Visualize the train set
plt.scatter(x_train, y_train, color='red') 
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# coefficient of model
m_slope = regressor.coef_
print(m_slope)

# intercept of model
c_intercept = regressor.intercept_
print(c_intercept)

# what model learn when y=12
y_12 = m_slope*12 + c_intercept
print(y_12)

# bias score (training datapoint)
bias_score = regressor.score(x_train, y_train)
print(bias_score)

# variance score (test datapoint)
variance_score = regressor.score(x_test, y_test)
print(variance_score)

# Stats integration to ML
# Mean
dataset.mean()
dataset["Salary"].mean()
dataset["YearsExperience"].mean()

# Median
dataset.median()

# Mode
dataset.mode()

# coefficient of variation (CV)
variation(dataset.values)

variation(dataset["Salary"])

# correlation between the attributes
dataset.corr()
print(dataset["Salary"].corr(dataset["YearsExperience"]))

# Skewness
# Positive Skew, Negative Skew, Zero Skew
dataset.skew()
dataset["Salary"].skew()

# Standard Error
# true mean
dataset.sem()

# Z-Score
dataset.apply(stats.zscore)

# Anova
# SSR (predicted - mean)
y_mean = np.mean(y)
SSR = np.sum((y_pred - y_mean)**2)
print(SSR)


# SSE 
y_= y[0:6]
SSE = np.sum((y_-y_pred)**2)
print(SSE)

# SST
mean_total = np.mean(dataset.values)
SST = np.sum((dataset.values-mean_total) ** 2)
print(SST)

# r2
r_square = 1 - SSR/SST
print(r_square)

# bias
bias = regressor.score(x_train, y_train)
print(bias)

# variance
variance = regressor.score(x_test, y_test)
print(variance)


# save the trained model to disk
filename = "linear_regression_model.pkl"

with open(filename, "wb") as file:
    pickle.dump(regressor, file)
    
print("Model has been pickled and saved as linear_regression_model.pkl")















