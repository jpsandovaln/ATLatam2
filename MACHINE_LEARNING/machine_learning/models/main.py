#
# @main.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from prediction import Prediction

if __name__ == '__main__':
    model = "vgg"
    folder_name = "images"
    word = "Bus"
    percentage = 50
    test = Prediction(folder_name, word, percentage)
    list = test.predict(model)

    for element in list:
        print(element.as_dict())
