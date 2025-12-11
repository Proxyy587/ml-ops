"""
The following are the fundamental steps for data preprocessing in machine learning:
1. Importing the libraries
2. Importing the dataset
3. Handling missing data
4. Encoding categorical data
5. Splitting the dataset into the Training set and Test set
6. Feature Scaling
"""

# import things

# dataset declaration

# do the things x and y shits

# impute the data if requreid

# encoding the categorical data

# labelcoding the dependent variable

# splitting the dataset into training and test set

# feature scaling (optional for some cases)


# Data Preprocessing Template
## Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
## Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
## Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)