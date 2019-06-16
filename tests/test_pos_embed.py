from unittest import TestCase
import numpy as np
from keras_transformer_xl.backend import keras
from keras_transformer_xl import PositionalEmbedding


class TestPositionalEmbedding(TestCase):

    def test_sample(self):
        model = keras.models.Sequential()
        model.add(PositionalEmbedding(10, input_shape=(4,)))
        model.compile('sgd', 'mse')
        x = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
        expected = np.array([[
            [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000],
            [0.8415, 0.1578, 0.0251, 0.0040, 0.0006, 0.5403, 0.9875, 0.9997, 1.0000, 1.0000],
            [0.9093, 0.3117, 0.0502, 0.0080, 0.0013, -0.4161, 0.9502, 0.9987, 1.0000, 1.0000],
            [0.1411, 0.4578, 0.0753, 0.0119, 0.0019, -0.9900, 0.8891, 0.9972, 0.9999, 1.0000],
        ]])
        predicted = model.predict(x)
        self.assertEqual((2, 4, 10), predicted.shape)
        self.assertTrue(np.allclose(expected, predicted[0], rtol=0.0, atol=1e-4), predicted)