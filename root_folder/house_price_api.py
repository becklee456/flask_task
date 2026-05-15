from flask import Flask, request, jsonify, send_from_directory
import joblib
import pandas as pd

# Load Pre-trained Model and Encoder
model = joblib.load("house_model.pkl")
encoder = joblib.load("location_encoder.pkl")
print("Model and encoder loaded successfully")

# Create Flask Application
app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Define Prediction API Endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        location = data['location']
        sqft = data['sqft']
        rooms = data['rooms']
        
        # Validate inputs
        if not isinstance(location, str) or location not in encoder.classes_:
            return jsonify({'error': 'Invalid location'}), 400
        if not isinstance(sqft, (int, float)) or sqft <= 0:
            return jsonify({'error': 'Invalid sqft, must be positive number'}), 400
        if not isinstance(rooms, int) or rooms <= 0:
            return jsonify({'error': 'Invalid rooms, must be positive integer'}), 400
        
        # Encode location
        location_encoded = encoder.transform([location])[0]
        
        # Prepare input
        input_data = pd.DataFrame([[location_encoded, sqft, rooms]], columns=['location', 'sqft', 'rooms'])
        
        # Predict
        prediction = model.predict(input_data)[0]
        
        return jsonify({'predicted_price': round(prediction, 2)})
    
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': 'Server error', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)