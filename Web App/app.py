from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

try:
    print("Model 1 loading...")
    model = tf.keras.models.load_model('models/NN_4input_1output.h5')
    # If you want to use the basic machine learning models
    #path_to_model = "models/Linear_SG_APP.pkl"  # Ensure the correct extension is used
    #model = joblib.load(path_to_model)
    print(f"Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.json
        
        # Extract the input values
        input_values = data.get('inputs')
        
        # Check if the input values have exactly 4 elements
        if not input_values or len(input_values) != 4:
            return jsonify({'error': 'Input must be a list of 4 numerical values'}), 400
        
        # Convert the input values to a 2D numpy array
        input_array = np.array([input_values])
        
        # Make the prediction
        prediction = model.predict(input_array)
        
        # Extract the output from the 2D array and convert to standard Python float
        output_value = float(prediction[0][0])
        
        # Return the result as JSON
        return jsonify({'prediction': output_value})
    
    except Exception as e:
        # Log the error and return a 500 error with the exception message
        print(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
