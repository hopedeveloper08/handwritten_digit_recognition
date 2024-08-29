import unittest
import tensorflow as tf
from model import load_model


class TestLoadModel(unittest.TestCase):
    def test_load_model(self):
        model = load_model()
        self.assertIsNotNone(model, "Model failed to load")
        self.assertTrue(isinstance(model, tf.keras.Model), "Loaded object is not a Keras model")

if __name__ == '__main__':
    unittest.main()
