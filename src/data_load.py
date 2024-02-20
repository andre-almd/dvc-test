'''DVC Stage to load data'''

import pandas as pd
from sklearn.datasets import load_iris

# Load data
iris = load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Save data in csv files
x.to_csv('data/input.csv', index=False)
y.to_csv('data/output.csv', index=False)
