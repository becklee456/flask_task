import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("houses.csv")

# Convert location text into numbers
encoder = LabelEncoder()
df["location"] = encoder.fit_transform(df["location"])

# Features and target
X = df[["location", "sqft", "rooms"]]
y = df["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model and encoder
joblib.dump(model, "house_model.pkl")
joblib.dump(encoder, "location_encoder.pkl")

print("Model trained successfully")