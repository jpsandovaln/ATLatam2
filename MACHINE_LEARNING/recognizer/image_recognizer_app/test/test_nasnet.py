from unittest import TestCase
from pathlib import Path

from ..model.nasnet import NasNet


class TestNasnet(TestCase):
    def test_nas_net(self):
        BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
        filepath = str(BASE_DIR) + '/resources_test/ml_image_test/001.jpg'
        d = NasNet()
        d.start()
        result = d.predict(filepath)
        print(result[0][0])

        expected = [('Eskimo_dog', float(0.57))]
        expected2 = ['Eskimo_dog', 0.5687792]
        self.assertListEqual(expected, result)
