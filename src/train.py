'''DVC Stage to train model'''

import yaml
import pandas as pd
from joblib import dump
from sklearn.svm import SVC

params = yaml.safe_load(open("params.yaml"))["train"]

# Load data
x_train = pd.read_csv('data/train.csv').to_numpy()
y_train = pd.read_csv('data/train_labels.csv').to_numpy().ravel()

model = SVC(C=params['c'], kernel=params['kernel'], gamma=params['gamma'])
model.fit(x_train, y_train)

# Save model with joblib
dump(model, 'data/model/model.joblib')
