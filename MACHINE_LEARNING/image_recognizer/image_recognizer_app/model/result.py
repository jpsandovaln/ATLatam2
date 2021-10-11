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
    def __init__(self, image, model, percentage, time, word):
        self.image = image
        self.model = model
        self.pecentage = percentage
        self.time = time
        self.word = word

    def as_dict(self):
        return {'imagen': self.image, 'modelo': self.model, 'confidence': str(self.pecentage),
                'time': self.time, 'object': self.word}
