import tensorflow as tf
import numpy as np
import os

class RecurrentNetworks():

    def __init__(self,path,window_size):
        self.model_path = os.path.join(path, 'hourly_lstm_weights_epochs_23')
        self.model = tf.keras.models.load_model(self.model_path)
        self.window_size = window_size

    def model_forecast(self, series):
        series = np.array(series)[np.newaxis,...]
        ds = tf.data.Dataset.from_tensor_slices(series)
        ds = ds.window(self.window_size + 1, shift=1, drop_remainder=True)
        ds = ds.flat_map(lambda w: w.batch(self.window_size + 1))
        ds = ds.batch(32).prefetch(1)
        forecast = self.model.predict(ds)[0][0]
        return forecast