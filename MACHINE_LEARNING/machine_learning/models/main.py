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
from prediccion import Prediccion

# noinspection SpellCheckingInspection
if __name__ == '__main__':
    # Definir el modelo de detección de objetos ("nasnet", "vgg", "resnet")
    modelo = "vgg"
    nombre_Carpeta = "images"
    #Crear un objeto tipo Prediccion que identificará cada imagen suministrada con el modelo seleccionado
    prueba = Prediccion(nombre_Carpeta)
    #Tener una lista de objetos con la información resultante de la detección
    lista = prueba.predict(modelo)

    for element in lista:
        print(element.as_dict())