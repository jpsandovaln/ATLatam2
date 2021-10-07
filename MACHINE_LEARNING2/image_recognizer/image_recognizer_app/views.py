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
from .models import Assets2
from .utils.checksum import Checksum



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
        filepath1 = str(BASE_DIR) + "/media"

        calculated_md5 = Checksum.md5(uploaded_file)

        if calculated_md5 == md5:
            print("es el mismo archivo")
        else:
            print("son archivos diferentes")

        # chek if the sent zip-file already exists (its MD% information in the DB
        if Assets2.objects.filter(checksum=md5):
            print('ya un archivo con el mismo checksum')
            previous_file = Assets2.objects.get(checksum=md5)
            with ZipFile('/'.join((previous_file.path, previous_file.name)), 'r') as zipObj:
                zipObj.extractall(previous_file.path)

            result = Prediction(previous_file.path + '/' + previous_file.name[:-4], word, percentage).predict(model)
            testing = [pred.as_dict() for pred in result]

            return JsonResponse(testing, safe=False)

        # if not, then save the file MD% into the DB and upload de file
        else:
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            asset = Assets2(name=uploaded_file.name, path=filepath1, checksum=md5)
            asset.save()
            with ZipFile('/'.join((filepath1, uploaded_file.name)), 'r') as zipObj:
                zipObj.extractall(filepath1)

            result = Prediction(filepath1 + '/' + uploaded_file.name[:-4], word, percentage).predict(model)
            testing = [pred.as_dict() for pred in result]

            # return HttpResponse(json.dumps(testing), 'application/json')
            return JsonResponse(testing, safe=False)
