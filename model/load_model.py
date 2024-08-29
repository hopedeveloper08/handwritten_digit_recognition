import tensorflow as tf
import os


def load_model():
    current_directory = os.getcwd()
    model_filename = 'best_model.keras'

    model_file_path = os.path.join(current_directory, 'model', model_filename)

    model = tf.keras.models.load_model(model_file_path)
    return model
