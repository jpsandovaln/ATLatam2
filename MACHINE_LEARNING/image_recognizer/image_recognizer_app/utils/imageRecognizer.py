
import os
from ..model.prediction import Prediction

class ImageRecognizer:
    @staticmethod
    def recognize(path, request):
        ImageRecognizer.validate(path)
        result = Prediction(path, request.POST['word'], request.POST['percentage']
                            ).predict(request.POST['model'])
        testing = [pred.as_dict() for pred in result]
        return testing

    @staticmethod
    def validate(path):
        if not os.path.isdir(path):
            raise Exception("Invalid folder path")
