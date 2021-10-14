from unittest import TestCase
from pathlib import Path

from ..model.nasnet import NasNet


class TestNasnet(TestCase):
    def test_nas_net(self):
        BASE_DIR = Path(__file__).parent.parent
        print(str(BASE_DIR))
        d = NasNet()
        d.start()
        result = d.predict(r'E:\AT-Bootcamp\102\Proyecto\ATLatam2\MACHINE_LEARNING\recognizer\media\images4\001.jpg')
        print(result[0][0])

        expected = ['Eskimo_dog', float(0.57)]
        self.assertListEqual(expected, result)
