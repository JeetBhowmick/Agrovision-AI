from flask import Flask, request, jsonify
import sys, os
sys.path.append(os.path.abspath("ML/Crop_recommendation"))

from ann_inference import predict_top3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/crop-recommend", methods=["POST"])
def crop_recommend():
    data = request.json

    required = ["N","P","K","temperature","humidity","ph","rainfall"]
    if not data or not all(k in data for k in required):
        return jsonify({"error": "Missing input fields"}), 400

    try:
        features = [
            data["N"], data["P"], data["K"],
            data["temperature"], data["humidity"], data["ph"], data["rainfall"]
        ]
        recommendations = predict_top3(features)
        return jsonify({"recommendations": recommendations})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
