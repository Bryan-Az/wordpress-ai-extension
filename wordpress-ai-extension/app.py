from flask import Flask, request, jsonify
import pickle
from PIL import Image
import numpy as np
import io
import base64
import logging

app = Flask(__name__)
app.debug = True
app.logger.setLevel(logging.DEBUG)
# Load the model
with open('kangaroo_classifier_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ensure image is part of the request
        if not request.json:
            logging.error("No JSON data received in request.")
            return jsonify({'error': 'No JSON data received.'}), 400

        if 'image' not in request.json:
            logging.error("No 'image' key found in the request JSON data.")
            return jsonify({'error': 'No image data received.'}), 400

        logging.info("'image' key found in the request JSON data. Proceeding to decode.")

        # Decode the Base64 encoded image
        image_data = base64.b64decode(request.json['image'])
        
        # Convert the decoded image data to an Image object
        image = Image.open(io.BytesIO(image_data)).convert('RGB')
        image = image.resize((256, 256))
        img_array = np.array(image).flatten().reshape(1, 196608)
        img_array = img_array / 255.0  # Normalize
        
        
        # Make prediction
        score = model.predict(img_array)
        logging.debug(f"Raw Model Output: {score}")
        if np.isscalar(score):
            return jsonify({"score": float(score)})
        elif len(score.shape) == 1:
            return jsonify({"score": float(score[0])})
        else:
            return jsonify({"score": float(score[0][0])})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

