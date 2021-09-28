from django.core.files.storage import FileSystemStorage
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from pathlib import Path
import json
from models.prediccion import Prediccion
from models.result import Result
from zipfile import ZipFile


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
        filepath1 = str(BASE_DIR) + "/media"

        with ZipFile('/'.join((filepath1, uploaded_file.name)), 'r') as zipObj:
            zipObj.extractall(filepath1)

        #filepath = str(BASE_DIR) + "/media/"

        #path = 'C:/Users/LCAS/PycharmProjects/PROG-102/Images'
        result = Prediccion(filepath1+'/'+uploaded_file.name[:-4]).predict(model)

        testing = {i: pred.as_dict() for i, pred in enumerate(result)}
        #testing = [pred.as_dict() for pred in result]
        print(testing)
        return HttpResponse(testing, 'application/json')
        #return JsonResponse(testing, safe=False)
