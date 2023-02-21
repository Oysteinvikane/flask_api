import joblib
from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import cross_origin

# Load the trained machine learning model from the file
model = joblib.load('model.joblib')

# Create a new Flask app
app = Flask(__name__)

# Enable CORS on the app
app.config['CORS_HEADERS'] = 'Content-Type'

# Define the feature names
feature_names = ['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    # Get the input data from the request
    input_data = request.json['input']

    # Create a DataFrame with the input data and feature names
    input_df = pd.DataFrame([input_data], columns=feature_names)

    # Make a prediction using the model
    prediction = model.predict(input_df)

    # Convert the prediction to a float
    prediction = float(prediction[0])

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run()
