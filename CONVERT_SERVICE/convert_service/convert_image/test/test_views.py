#
# @test_views.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from unittest import TestCase
from convert_service.convert_image.model.convert_image import ConvertImage
from convert_service.convert_image.model.convert_image_params import ConvertImageParams


class TestImageConverter(TestCase):
    """ Class to test methods of ImageConvert """

    def test_post(self):
        param = ConvertImageParams('', 'true', 'true', '', '400,400', '', 'true', '',
                                   '', '', '', 'implode', 'vignette')
        result_error = {
            "status": "ERROR",
            "imageOutput": "NOT IMAGE"
        }

        image = ConvertImage()
        image.convert(param)

        self.fail()
