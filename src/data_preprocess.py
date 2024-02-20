'''DVC Stage to Pre Process data'''

import yaml
import pandas as pd
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

params = yaml.safe_load(open("params.yaml"))["data_preprocess"]

# Load data
x = pd.read_csv('data/input.csv')
y = pd.read_csv('data/output.csv')

# Splitting the data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=params['test_size'],
                                                    random_state=params['random_state'],
                                                    stratify=y)

# Preprocessing (Standardization)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Save Scaler with joblib
dump(scaler, 'data/model/scaler.joblib')
