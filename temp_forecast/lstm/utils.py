import tensorflow as tf
from .apps import LstmConfig
import numpy as np
import os

class RecurrentNetworks():

    def __init__(self,window_size):
        self.model = LstmConfig.model
        self.window_size = window_size

    def model_forecast(self, series):
        series = np.array(series)[np.newaxis,...]
        ds = tf.data.Dataset.from_tensor_slices(series)
        ds = ds.window(self.window_size + 1, shift=1, drop_remainder=True)
        ds = ds.flat_map(lambda w: w.batch(self.window_size + 1))
        ds = ds.batch(32).prefetch(1)
        forecast = self.model.predict(ds)[0][0]
        return forecast