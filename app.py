from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np
# Initialize the Flask app
app = Flask(__name__)

# Load the model
with open('model2.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the request
        data = request.json
        # Assuming the input data is passed as a list of features
        input_df = pd.DataFrame(data)

        # Use the model to make a prediction
        prediction = model.predict(input_df)
        d_v_d=pd.read_csv('Doctor_Versus_Disease.csv')
        l=[]
        for p in prediction:
            l.append(d_v_d[d_v_d['Disease']==p]['Doctor Type'].values.tolist())
        doc_predict=np.array(l).flatten().tolist()
        # Return the prediction as a JSON response
        return jsonify({'Disease': prediction.tolist(),'Doctor Type':doc_predict})
    
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
