from django.apps import AppConfig
from django.conf import settings
import tensorflow as tf
from tensorflow.keras.models import model_from_json
import os

class LstmConfig(AppConfig):
    name = 'lstm'

    with open(os.path.join(settings.ARTIFACTS, 'model.json'),'r') as json_file:
        model_json = json_file.read()
        model = model_from_json(model_json)
        model_h5 = os.path.join(settings.ARTIFACTS, 'model.h5')
        # load weights into new model
        model.load_weights(model_h5)

