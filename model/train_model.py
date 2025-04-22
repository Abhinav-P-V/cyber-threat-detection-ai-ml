import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
from model.features import extract_features

df = pd.read_csv("data/logs.csv")
X = extract_features(df)

model = IsolationForest(contamination=0.2, random_state=42)
model.fit(X)

joblib.dump(model, "model/insider_threat_model.pkl")
print("✅ Model trained and saved.")
