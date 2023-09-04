from flask import Flask, request, jsonify
import pickle
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load the model
with open('kangaroo_classifier_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ensure image is part of the request
        if 'image' not in request.files:
            return jsonify({"error": "No image data received."}), 400

        image = request.files['image']
        img = Image.open(image).convert('RGB')
        img = img.resize((224, 224))
        img_array = np.array(img)
        img_array = img_array / 255.0  # Normalize
        img_array = img_array.reshape(1, 224, 224, 3)
        
        # Make prediction
        score = model.predict(img_array)
        return jsonify({"score": float(score[0][0])})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

