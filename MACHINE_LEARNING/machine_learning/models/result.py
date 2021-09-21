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
    def __init__(self, imagen, porcentaje, modelo, prediccion):
        self.imagen = imagen
        self.porcentaje = porcentaje
        self.modelo = modelo
        self.prediccion = prediccion

    def __str__(self):
        cadena = "la imagen {} contiene {} con un {:.4} % usando el {}".format(
            self.imagen, self.prediccion, self.porcentaje, self.modelo)
        print(cadena)
