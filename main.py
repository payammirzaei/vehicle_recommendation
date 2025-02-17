from src.data_preprocessing import load_and_preprocess_data
from src.model_training import build_and_train_model
from src.recommender import recommend_vehicle

# Load and preprocess data
X_train, X_test, y_train, y_test, encoders, data = load_and_preprocess_data("data/vehicles.csv")

# Train the model
model = build_and_train_model(X_train, y_train)

# User preferences
user_preferences = {
    "price": 20000,
    "type": "SUV",
    "fuel": "Petrol",
    "engine_capacity": 2.0,
    "transmission": "Automatic",
    "seats": 5,
    "mileage": 14.0,
    "brand": "Toyota"
}

# Recommend a vehicle
try:
    recommended_vehicle = recommend_vehicle(model, encoders, data, user_preferences)
    print("Recommended Vehicle:")
    print(recommended_vehicle)
except ValueError as e:
    print(f"Error: {e}")

