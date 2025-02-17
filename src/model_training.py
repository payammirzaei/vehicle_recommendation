import tensorflow as tf

def build_and_train_model(X_train, y_train):
    # Build the neural network model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(16, input_shape=(X_train.shape[1],), activation='relu'),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(1, activation='linear')  # Output layer
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])

    # Train the model
    model.fit(X_train, y_train, epochs=20, batch_size=2, verbose=1)

    return model
