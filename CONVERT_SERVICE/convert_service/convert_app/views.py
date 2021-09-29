from django.core.files.storage import FileSystemStorage
from pathlib import Path
from django.views import View
from django.http import HttpResponse
from .model.ffmpeg.ffmpeg_execute import ffmpegexecute
from .model.ffmpeg.img_compresor import zip_dir
import json


# Create your views here.


class Converter(View):

    def post(self, request):
        if request.method == 'POST':
            # Upload the file
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()

            # Save the file
            fs.save(uploaded_file.name, uploaded_file)
            file = uploaded_file.name

            # Set the path to the requested file
            filename = file
            BASE_DIR = Path(__file__).resolve().parent.parent
            filepath = str(BASE_DIR) + "/media/" + filename

            # Execute the ffmpeg model and zip compresor
            ffmpegexecute(filepath)
            zip_dir('images', filename)

            return HttpResponse(json.dumps(filename), 'application/json')

        return HttpResponse("Please, used method POST")
