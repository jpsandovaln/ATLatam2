#
# @resnet.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input
from keras.applications.resnet50 import decode_predictions
import numpy as np


# noinspection SpellCheckingInspection
class ResNet:
    """Modelo ResNet50"""
    def __init__(self):
        # Definir el modelo preentrenado
        self.name = 'ResNet50'
        self.model = ResNet50(weights='imagenet', include_top=True)

    # noinspection SpellCheckingInspection
    # Método que realiza la predicción de objetos en una imagen
    def predict(self, img_path):
        # Preprocesamiento
        original = image.load_img(img_path, target_size=(224, 224))
        numpy_image = image.img_to_array(original)
        image_batch = np.expand_dims(numpy_image, axis=0)
        processed_image = preprocess_input(image_batch)
        # Reconocimiento
        preds = self.model.predict(processed_image)
        # Seleccionar las dos primeras predicciones
        pred_class = decode_predictions(preds, top=2)[0][0]

        return [(pred_class[1], pred_class[2])]
