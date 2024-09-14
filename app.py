from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)

# Set CORS to allow requests from specific origins (e.g., localhost)
CORS(app,origins="*")

# Load the model
with open('model2.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the request
        data = request.json

        # Convert data to a pandas DataFrame
        input_df = pd.DataFrame(data)

        # Use the model to make a prediction
        prediction = model.predict(input_df)

        # Map the predictions to doctor types from the CSV
        d_v_d = pd.read_csv('Doctor_Versus_Disease.csv')
        l = []
        for p in prediction:
            doctor_type = d_v_d[d_v_d['Disease'] == p]['Doctor Type'].values.tolist()
            l.append(doctor_type)
        
        doc_predict = np.array(l).flatten().tolist()

        # Return the prediction as a JSON response
        return jsonify({'disease': prediction.tolist(), 'doctor_type': doc_predict})
    
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
