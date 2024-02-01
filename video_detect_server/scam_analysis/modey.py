import tensorflow as tf


class ScamAnalysisModel:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        print(self.model)
