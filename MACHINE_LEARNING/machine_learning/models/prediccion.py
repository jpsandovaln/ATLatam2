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
import os
from nasnet import NasNet
from resnet import ResNet
from result import Result
from vgg16 import Vgg16


# noinspection SpellCheckingInspection
class Prediccion:
    """Lleva a cabo la detección de objeto en todas las imágenes de un directorio"""
    def __init__(self, folder):
        self.modelos = {'nasnet': NasNet(), 'resnet': ResNet(), 'vgg': Vgg16()}
        self.folder = folder
        self.imagenes = os.listdir(folder)

    # noinspection SpellCheckingInspection
    def predict(self, modelo):
        # Instanciación del modelo escogigo para hacer la detección
        model = self.modelos[modelo]
        # Lista que almacenará los objetos resultado
        list_obj = []
        for imagen in self.imagenes:
            # Se ejecuta la predicción sobre cada imagen del directorio provisto
            pre = model.predict('/'.join((self.folder, imagen)))
            # Se conservan solo las predicciones con más de 70% de precisión como objetos Result()
            if pre[0][2] > 0.7:
                resultado = Result(imagen, pre[0][2] * 100, model.__doc__, pre[0][1])
                list_obj.append(resultado)

        return list_obj
