import tensorflow as tf
from .apps import LstmConfig
from django.conf import settings
import numpy as np
import pandas as pd
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

    def process_data(self,df):
        df['Date/Time'] = pd.to_datetime(df['Date/Time'])
        cols = ['Month','Day','Dew Point Temp (°C)','Rel Hum (%)','Wind Spd (km/h)','Stn Press (kPa)']
        df = df.sort_values(by='Date/Time',ignore_index=True)
        series = df[cols].values[:]
        return series

    def model_multi_forecast(self, series):
        ds = tf.data.Dataset.from_tensor_slices(series)
        ds = ds.window(self.window_size + 1, shift=1, drop_remainder=True)
        ds = ds.flat_map(lambda w: w.batch(self.window_size + 1))
        ds = ds.batch(32).prefetch(1)
        forecast = self.model.predict(ds)
        rnn_forecast = forecast[:,0]
        return rnn_forecast

def handle_uploaded_file(f):
    with open(os.path.join(os.path.dirname(__file__), 'file.csv'), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


