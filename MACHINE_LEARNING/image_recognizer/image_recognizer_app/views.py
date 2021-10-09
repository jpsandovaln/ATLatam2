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


class Recognizer(View):
    """ Machine Learning Endpoint, call machine learning modules with
        receive parameters and recognize objects from a zipped image folder"""
    def post(self, request):

        uploaded_file = request.FILES['file']
        word = request.POST['word']
        model = request.POST['model']
        percentage = request.POST['percentage']
        md5 = request.POST['md5']

        BASE_DIR = Path(__file__).resolve().parent.parent

        # chek if the sent zip-file already exists
        verified = Checker.check(BASE_DIR, uploaded_file, md5)
        # Verify if client send wrong MD5 checksum
        if verified == -1:
            return JsonResponse("MD5 sent DO NOT correspond to uploaded file's MD5", safe=False)

        else:
            images_path = Unzip.extract(verified['path'], verified['filename'])
            result = Prediction(images_path, word, percentage).predict(model)
            testing = [pred.as_dict() for pred in result]

            return JsonResponse(testing, safe=False)
