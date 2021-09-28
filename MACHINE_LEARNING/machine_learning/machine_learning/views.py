from django.core.files.storage import FileSystemStorage
from django.views import View
from django.http import HttpResponse
from pathlib import Path
from models.prediccion import Prediccion
from zipfile import ZipFile
from models.result import Result
import json
from django.http import JsonResponse


class Recognizer(View):

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

        # Call ML Prediction
        result = Prediccion(filepath1+'/'+uploaded_file.name[:-4], word, percentage).predict(model)

        #testing = {i: pred.as_dict() for i, pred in enumerate(result)}
        testing = [pred.as_dict() for pred in result]
        print(testing)
        return HttpResponse(json.dumps(testing), 'application/json')
        # return JsonResponse(testing, safe=False)
