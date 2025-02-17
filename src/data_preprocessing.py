import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Encode categorical variables and store encoders
    encoders = {}
    for col in ['type', 'fuel', 'transmission', 'brand']:
        encoders[col] = LabelEncoder()
        data[col] = encoders[col].fit_transform(data[col])

    # Features and target
    X = data[['price', 'type', 'fuel', 'engine_capacity', 'transmission', 'seats', 'mileage', 'brand']]
    y = data['vehicle_id']

    # Split into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, encoders, data
