#
# @video_converter.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path
import mimetypes
import datetime
import json
import os

from models.ffmpeg.frame_extractor import FrameExtractor
from models.ffmpeg.python_parameters import PythonParameters
from models.ffmpeg.folder_check import FolderCheck
from models.ffmpeg.fmex_execute import Execute

#In the file settings.py in the list of TEMPLATES (line 54) in the part of DIR, I specified the folder of the templates. So you only use loader.get_template('name_file.html') to load a template.
#In the file settings.py, in the line 130 i specified the path to save the files.

#1: https://www.youtube.com/playlist?list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB - Course of Django
#2: https://www.youtube.com/watch?v=T7ckAimOtZg - How return a json.
#3: https://es.stackoverflow.com/questions/34904/cuando-debo-usar-los-m%C3%A9todos-post-y-get
#4: https://www.youtube.com/watch?v=Zx09vcYq1oc&t - Upload a file
#5: https://medium.com/@Bartleby/django-postman-403-csrf-verification-failed-49b05ca79e8e
#6: https://www.youtube.com/watch?v=eWEgUcHPle0&t=334s - CSRF Token



# User Interface
def index(request):

    date = datetime.datetime.now()
    list_models = ["ResNet50","VGG16"]
    text = "Complete the fields below:"

    dictionary = {"Text": text, "Date": date, "Lista_Modelos": list_models}
    return render(request, 'index.html', dictionary)



@csrf_exempt # Unsafe way - Implement csrf token in the nexts commits. Please read resource #5.
def upload(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file) # Save the file

        # I create a dictionary
        diccionario = {}
        diccionario['file'] = uploaded_file.name
        diccionario['word'] = request.POST["word"]
        diccionario['model'] = request.POST["model"]
        diccionario['percentage'] = request.POST["percentage"]

        # Set the path to the requested file
        filename = diccionario['file']
        BASE_DIR = Path(__file__).resolve().parent.parent
        filepath = str(BASE_DIR) + "/media/" + filename

        # Revisamos que la carpeta images exista o la creamos
        folderCheck = FolderCheck
        folderCheck.execute()

        # Pasamos los parametros
        pythonParameters = PythonParameters(filepath, 'images/%04d.jpg')  # Video input, Frames Output

        # Iniciamos el extractor de frames
        frameExtractor = FrameExtractor()

        # Le damos los parametros y lo guardamos en la variable command
        command = frameExtractor.build(pythonParameters)

        # Ejecutamos nuestra clase fmex_execute
        execute = Execute(command)
        print(execute.run())


        # I convert the dictionary to json
        return HttpResponse(json.dumps(diccionario), 'application/json')

    return HttpResponse("Please, used method POST")



def download(request):

    if request.method == 'GET':
        filename = request.GET["file_name"]

        #Set the path to the requested file
        BASE_DIR = Path(__file__).resolve().parent.parent
        filepath = str(BASE_DIR) + "/media/" + filename

        #Open the file in reading and binary mode.
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value

        return response
