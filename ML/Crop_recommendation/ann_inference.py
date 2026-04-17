import numpy as np
import joblib
from tensorflow.keras.models import load_model
import os

# Absolute path handling (CRITICAL FIX)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "crop_ann_model.keras")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")
encoder_path = os.path.join(BASE_DIR, "label_encoder.pkl")

# Load artifacts once
model = load_model(model_path)
scaler = joblib.load(scaler_path)
label_encoder = joblib.load(encoder_path)

def predict_top3(features):
    """
    features = [N, P, K, temperature, humidity, ph, rainfall]
    """

    features = np.array(features).reshape(1, -1)
    scaled = scaler.transform(features)

    probabilities = model.predict(scaled)[0]

    top3_idx = np.argsort(probabilities)[-3:][::-1]
    crops = label_encoder.inverse_transform(top3_idx)
    confidences = probabilities[top3_idx]

    return [
        {
            "crop": crops[i],
            "confidence": round(float(confidences[i]) * 100, 2)
        }
        for i in range(3)
    ]
