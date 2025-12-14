import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(r"C:\Users\mikun\Downloads\Data.csv")

x = data.iloc[:, :-1].values
y = data.iloc[:, 3].values



