from django.core.files.storage import FileSystemStorage
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from pathlib import Path
import json
from models.prediccion import Prediccion
from models.result import Result


class Recognizer(View):

    def post(self, request):
        print(":*:*:*")

        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        word = request.POST['word']
        model = request.POST['model']
        percentage = request.POST['percentage']

        BASE_DIR = Path(__file__).resolve().parent.parent
        filepath = str(BASE_DIR) + "/media/"

        #path = 'C:/Users/LCAS/PycharmProjects/PROG-102/Images'
        result = Prediccion(filepath).predict(model)
        preds =[]
        if len(result) >0:
            for prediction in result:
                preds.append(prediction.as_dict())



        return HttpResponse('hola', 'application/json')
        #return JsonResponse(preds, safe=False)
