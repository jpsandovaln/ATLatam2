#
# @prediction.py Copyright (c) 2021 Jalasoft.
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
from .nasnet import NasNet
from .resnet import ResNet
from .result import Result
from .vgg16 import Vgg16
from .yolo import Yolo


class Prediction:
    """Performs object detection on all images in a directory"""

    def __init__(self, folder):
        self.models = {'nasnet': NasNet(), 'resnet': ResNet(), 'vgg': Vgg16(), 'yolo': Yolo()}
        self.folder = folder
        self.images = os.listdir(folder)

    def predict(self, model):
        model = self.models[model]
        list_obj = []
        for image in self.images:
            pre = model.predict('/'.join((self.folder, image)))
            result = Result(image, model.name, pre)
            list_obj.append(result)

        return list_obj
