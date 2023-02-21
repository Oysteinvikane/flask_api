from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os

# Load the trained machine learning model from the file
model = joblib.load(os.path.join(os.path.dirname(__file__), 'model.joblib'))

# Create a new Flask app
app = Flask(__name__)

# Define the feature names
feature_names = ['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']

@app.route('/api/predict', methods=['POST'])
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

# Run the Flask app on a production-ready server
if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
