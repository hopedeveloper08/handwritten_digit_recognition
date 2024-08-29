from flask import Flask, jsonify, render_template
import numpy as np
import tensorflow as tf
from model import load_model, preprocess_image


app = Flask(__name__)
model = load_model()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    path = 'templates\digit.png'
    image = preprocess_image(path)
    prediction = model.predict(image)
    digit = np.argmax(prediction)
    return jsonify({'digit': int(digit)})


@app.route('/clear', methods=['POST'])
def clear():
    return jsonify({'status': 'cleared'})


if __name__ == '__main__':
    app.run(debug=True)
