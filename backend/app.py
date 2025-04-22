import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify
import pandas as pd
import joblib
from model.features import extract_features

# Load trained model
model = joblib.load("model/insider_threat_model.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])
        features = extract_features(input_df)
        prediction = model.predict(features)[0]
        result = "Anomaly" if prediction == -1 else "Normal"
        return jsonify({'threat': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
