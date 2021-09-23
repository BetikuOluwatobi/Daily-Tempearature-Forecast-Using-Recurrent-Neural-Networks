import tensorflow as tf
from tensorflow.keras.models import model_from_json
import numpy as np
import os

class RecurrentNetworks():

    def __init__(self,path,window_size):
        self.json_file = open(os.path.join(path, 'model.json'),'r')
        self.model_h5 = os.path.join(path, 'model.h5')
        self.model_json = json_file.read()
        self.json_file.close()
        self.model = model_from_json(self.model_json)
        # load weights into new model
        self.model.load_weights(self.model_h5)
        self.window_size = window_size

    def model_forecast(self, series):
        series = np.array(series)[np.newaxis,...]
        ds = tf.data.Dataset.from_tensor_slices(series)
        ds = ds.window(self.window_size + 1, shift=1, drop_remainder=True)
        ds = ds.flat_map(lambda w: w.batch(self.window_size + 1))
        ds = ds.batch(32).prefetch(1)
        forecast = self.model.predict(ds)[0][0]
        return forecast