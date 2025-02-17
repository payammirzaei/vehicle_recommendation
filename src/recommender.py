import pandas as pd

def recommend_vehicle(model, encoders, data, user_input):
    # Encode categorical inputs using the stored encoders
    for col in ['type', 'fuel', 'transmission', 'brand']:
        if user_input[col] in encoders[col].classes_:
            user_input[col] = encoders[col].transform([user_input[col]])[0]
        else:
            # Handle unseen labels (optional: set to default or raise error)
            raise ValueError(f"'{user_input[col]}' is an unseen label for '{col}' column")

    # Create DataFrame for user input
    user_df = pd.DataFrame([user_input])

    # Make prediction
    prediction = model.predict(user_df)
    recommended_vehicle_id = round(prediction[0][0])

    # Find the recommended vehicle
    recommended_vehicle = data[data['vehicle_id'] == recommended_vehicle_id]
    return recommended_vehicle
