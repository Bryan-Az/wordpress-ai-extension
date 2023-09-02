from flask import Flask, request, jsonify
import pymysql
from sklearn.externals import joblib
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load('kangaroo_classifier_model.pki')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the POST request
    image = Image.open(request.files['file'])

    # Preprocess the image
    image = image.resize((256, 256))
    image = np.array(image)
    image = image.reshape(1, -1)

    # Predict the score
    score = model.predict(image)

    # Connect to the database
    db = pymysql.connect("db", "wordpress", "wordpress", "wordpress")

    # Insert the score into the database
    with db.cursor() as cursor:
        sql = "INSERT INTO scores (score) VALUES (%s)"
        cursor.execute(sql, (score,))

    db.commit()
    db.close()

    # Return the score
    return jsonify({'score': score.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
