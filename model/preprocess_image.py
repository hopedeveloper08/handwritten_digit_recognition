import numpy as np
from PIL import Image


def preprocess_image(file):
    img = Image.open(file).convert('L')
    img = img.resize((28, 28))
    img_array = np.array(img)
    img_array = 255 - img_array
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=(0, -1))
    return img_array
