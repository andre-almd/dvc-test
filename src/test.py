'''DVC Stage to test model'''

import json
import pandas as pd
from joblib import load
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score

# Load model
model = load('data/model/model.joblib')

# Load data
x_test = pd.read_csv('data/test.csv').to_numpy()
y_test = pd.read_csv('data/test_labels.csv').to_numpy().ravel()

# Evaluate model
y_pred_test = model.predict(x_test)
test_accuracy = accuracy_score(y_test, y_pred_test)

recall = recall_score(y_test, y_pred_test, average='macro')
cm = confusion_matrix(y_test, y_pred_test)

# Save metrics in a json file
metrics = {
    'accuracy': test_accuracy,
    'recall': recall,
    'confusion_matrix': cm.tolist()
    }

with open('metrics/model_metrics.json', 'w') as f:
    json.dump(metrics, f)
