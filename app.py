from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
from model import load_model


app = Flask(__name__)
model = load_model()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            file.save(filename)
            image = Image.open(filename).convert('L').resize((28, 28))
            image = np.array(image) / 255.0
            image = image.reshape(1, 28, 28, 1)
            prediction = model.predict(image)
            result = np.argmax(prediction)
            return render_template('index.html', result=result)
    return render_template('index.html', result=None)


if __name__ == '__main__':
    app.run(debug=True)
