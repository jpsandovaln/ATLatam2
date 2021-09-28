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
# noinspection SpellCheckingInspection
class Result:
    """ Almacena ls información de los resultados de la detección de objetos"""
    def __init__(self, imagen, modelo, predictions):
        self.imagen = imagen
        self.modelo = modelo
        self.predictions_list = predictions

    def as_dict(self):
        return {'imagen': self.imagen, 'modelo': self.modelo, 'predictions_list': self.predictions_list}