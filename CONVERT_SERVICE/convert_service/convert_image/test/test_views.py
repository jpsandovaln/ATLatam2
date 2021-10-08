from unittest import TestCase

from convert_service.convert_image.model.convert_image import ConvertImage
from convert_service.convert_image.model.convert_image_params import ConvertImageParams


class TestImageConverter(TestCase):
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
