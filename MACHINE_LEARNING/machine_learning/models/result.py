#
# @result.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

class Result:
    """ Stores the information of the object detection results"""
    def __init__(self, image, model, predictions):
        self.image = image
        self.model = model
        self.predictions_list = predictions

    def as_dict(self):
        return {'image': self.image, 'model': self.model, 'predictions_list': self.predictions_list}
