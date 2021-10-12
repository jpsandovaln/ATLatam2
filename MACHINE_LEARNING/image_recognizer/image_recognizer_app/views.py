#
# @views.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from django.views import View
from django.http import JsonResponse
from pathlib import Path
from .model.prediction import Prediction
from .utils.checker import Checker
from .utils.unzip import Unzip
from django.http import HttpResponse
from .utils.imageRecognizer import ImageRecognizer

class Recognizer(View):
    """ Machine Learning Endpoint, call machine learning modules with
        received parameters and recognize objects from a zipped image folder"""

    def post(self, request):

        BASE_DIR = Path(__file__).resolve().parent.parent
        try:
            verified = Checker.check(BASE_DIR, request.FILES['file'], request.POST['md5'])

            images_path = Unzip.extract(verified['path'], verified['filename'])

            testing = ImageRecognizer.recognize(images_path, request)

            return JsonResponse(testing, safe=False)

        except Exception as error:
            return HttpResponse(error, "application/json")
