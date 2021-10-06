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
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.http import JsonResponse
from django.http import HttpResponse
import json
from pathlib import Path
from .model.prediction import Prediction
from zipfile import ZipFile


class Recognizer(View):
    """ Machine Learning Endpoint, call machine learning modules with
        receive parameters and recognize objects from a zipped image folder"""
    def post(self, request):

        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        word = request.POST['word']
        model = request.POST['model']
        percentage = request.POST['percentage']

        BASE_DIR = Path(__file__).resolve().parent.parent
        filepath1 = str(BASE_DIR) + "/media"

        # unzip FIle
        with ZipFile('/'.join((filepath1, uploaded_file.name)), 'r') as zipObj:
            zipObj.extractall(filepath1)

        # Call ML Prediction and get results
        result = Prediction(filepath1+'/'+uploaded_file.name[:-4], word, percentage).predict(model)
        testing = [pred.as_dict() for pred in result]

        # return HttpResponse(json.dumps(testing), 'application/json')
        return JsonResponse(testing, safe=False)
