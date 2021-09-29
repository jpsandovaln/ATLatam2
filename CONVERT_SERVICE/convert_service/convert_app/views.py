#
# @views.py Copyright (c) 2021 Jalasoft.
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
