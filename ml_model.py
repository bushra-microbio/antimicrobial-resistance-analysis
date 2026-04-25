# Machine Learning Model for Antimicrobial Resistance 
# Author: Bushra Mumtaz

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Sample dataset
data = {
    "Antibiotic": ["Ampicillin", "Ciprofloxacin", "Gentamicin", "Ceftriaxone", "Meropenem"],
    "Resistance_Rate": [80, 45, 30, 60, 10],
    "Resistant": [1, 1, 0, 1, 0]  # 1 = Resistant, 0 = Sensitive
}

df = pd.DataFrame(data)

# Features and labels
X = df[["Resistance_Rate"]]
y = df["Resistant"]

# Model
model = RandomForestClassifier()
model.fit(X, y)

# Prediction
prediction = model.predict([[50]])

print("Prediction for resistance at 50% rate:", prediction)
