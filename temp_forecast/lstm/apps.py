from django.apps import AppConfig
from django.conf import settings
import tensorflow as tf
import os

class LstmConfig(AppConfig):
    name = 'lstm'
    model = tf.keras.models.Sequential([
        tf.keras.layers.Lambda(lambda x: x * 0.1,
                            input_shape=[None,6]),
        tf.keras.layers.Conv1D(filters=32, kernel_size=5,
                            strides=1, padding="causal",
                            activation="relu"),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64,activation='relu',return_sequences=True,input_shape=[None])),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64,activation='relu', return_sequences=True)),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32,activation='relu')),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.Dense(16,activation='relu'),
        tf.keras.layers.Dense(1),
        tf.keras.layers.Lambda(lambda x: x * 10)
        ])

    optimizer = tf.keras.optimizers.Adam(learning_rate=0.00034)

    model.compile(loss=tf.keras.losses.Huber(), optimizer=optimizer,metrics=[tf.keras.metrics.RootMeanSquaredError()])

    model_h5 = os.path.join(settings.STATICFILES_DIR, 'model.h5')
    # load weights into new model
    model.load_weights(model_h5)

