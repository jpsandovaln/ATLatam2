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

from urllib import request
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import FileSystemStorage
from pathlib import Path
from django.views import View
from django.http import HttpResponse
from .model.ffmpeg.ffmpeg_execute import ffmpegexecute
from .model.ffmpeg.img_compresor import zip_dir

from .model.convert_image.convert_image import Param, ConvertImage

import json


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


class ImageConverter(View):
    def post(self, request):
        if request.method == 'POST':
            # Upload the file
            uploaded_file = request.FILES['file']
            grayscale = request.POST['grayscale']
            blur = request.POST['blur']
            adaptive_sharpen = request.POST['adaptive_sharpen']
            resize = request.POST['resize']
            flip = request.POST['flip']
            flop = request.POST['flop']
            rotate = request.POST['rotate']
            noise = request.POST['noise']
            charcoal = request.POST['charcoal']
            matrix = request.POST['matrix']
            implode = request.POST['implode']
            vignette = request.POST['vignette']

            print(grayscale)
            fs = FileSystemStorage()

            # Save the file
            fs.save(uploaded_file.name, uploaded_file)
            file = uploaded_file.name

            # Set the path to the requested file
            filename = file
            BASE_DIR = Path(__file__).resolve().parent.parent
            filepath = str(BASE_DIR) + "/media/" + filename

            # Create object image to convert image
            image = ConvertImage()
            param = Param(filepath, grayscale, blur, adaptive_sharpen, resize, flip, flop, rotate, noise, charcoal,
                          matrix, implode,
                          vignette)
            image.convert(param)

            # get download path
            final_path = image.get_final_path()
            print(final_path)
            result = {
                "status": "OK",
                "imageOutput": "http://" + str(get_current_site(request).domain) + "/" + final_path
            }

            return HttpResponse(json.dumps(result), 'application/json')

        return HttpResponse("Please, used method POST")
