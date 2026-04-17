import numpy as np
import pickle
from tensorflow.keras.models import load_model

# 1. Load model & preprocessors once
model = load_model("crop_ann_model.h5")

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)


def predict_top3(farmer_input):
    """
    Input: dict with keys N, P, K, temperature, humidity, ph, rainfall
    Output: list of dicts [{crop: str, confidence: float}, ...]
    """
    # Convert to array
    input_array = np.array([[
        farmer_input["N"],
        farmer_input["P"],
        farmer_input["K"],
        farmer_input["temperature"],
        farmer_input["humidity"],
        farmer_input["ph"],
        farmer_input["rainfall"]
    ]])

    # Scale
    input_scaled = scaler.transform(input_array)

    # Predict
    probabilities = model.predict(input_scaled)[0]

    # Top 3
    top_3_indices = np.argsort(probabilities)[-3:][::-1]
    top_3_crops = label_encoder.inverse_transform(top_3_indices)
    top_3_probs = probabilities[top_3_indices]

    # Prepare JSON-friendly output
    result = []
    for i in range(3):
        result.append({
            "crop": str(top_3_crops[i]),
            "confidence": round(float(top_3_probs[i]*100), 2)
        })

    return result
