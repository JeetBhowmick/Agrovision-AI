import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical

# 1. Load dataset
data = pd.read_csv("Crop_Recommendation.csv")

X = data.drop("Crop", axis=1)
y = data["Crop"]

# 2. Encode labels (same logic as training)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
y_categorical = to_categorical(y_encoded)

# 3. Train-test split (same random_state as training)
X_train, X_test, y_train, y_test = train_test_split(
    X, y_categorical, test_size=0.2, random_state=42, stratify=y_encoded
)

# 4. Load scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

X_test = scaler.transform(X_test)

# 5. Load trained model
model = load_model("crop_ann_model.h5")

# 6. Predict
y_pred_prob = model.predict(X_test)
y_pred = np.argmax(y_pred_prob, axis=1)
y_true = np.argmax(y_test, axis=1)

# 7. Evaluation
accuracy = accuracy_score(y_true, y_pred)
print("\nModel Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_true, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_true, y_pred))
