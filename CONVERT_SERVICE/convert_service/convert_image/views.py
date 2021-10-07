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

# Create your views here.
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.http import HttpResponse
from pathlib import Path
import json
from .model.convert_image import ConvertImage
from .model.convert_image_params import ConvertImageParams


class ImageConverter(View):

    def post(self, request):
        if request.method == 'POST':
            try:
                # Upload the file
                uploaded_file = request.FILES['file']
            except:
                result_error = {
                    "status": "ERROR",
                    "imageOutput": "NOT IMAGE"
                }
                return HttpResponse(json.dumps(result_error), 'application/json')

            grayscale = self.except_request(request, 'grayscale')
            blur = self.except_request(request, 'blur')
            adaptive_sharpen = self.except_request(request, 'adaptive_sharpen')
            resize = self.except_request(request, 'resize')
            flip = self.except_request(request, 'flip')
            flop = self.except_request(request, 'flop')
            rotate = self.except_request(request, 'rotate')
            noise = self.except_request(request, 'noise')
            charcoal = self.except_request(request, 'charcoal')
            matrix = self.except_request(request, 'matrix')
            implode = self.except_request(request, 'implode')
            vignette = self.except_request(request, 'vignette')

            fs = FileSystemStorage()
            # Save the file
            fs.save(uploaded_file.name, uploaded_file)
            file = uploaded_file.name

            # Set the path to the requested file
            filename = file
            BASE_DIR = Path(__file__).resolve().parent.parent
            filepath = str(BASE_DIR) + "/media/" + filename

            # Create object image to convert image
            param = ConvertImageParams(filepath, grayscale, blur, adaptive_sharpen, resize, flip, flop, rotate,
                                       noise,
                                       charcoal,
                                       matrix, implode,
                                       vignette)

            try:
                image = ConvertImage()
                image.convert(param)

                # get download path
                final_path = image.get_final_path()
                result = {
                    "status": "OK",
                    "imageOutput": "http://" + str(get_current_site(request).domain) + "/" + final_path
                }
                return HttpResponse(json.dumps(result), 'application/json')
            except:
                result_error = {
                    "status": "ERROR",
                    "imageOutput": "NOT IMAGE"
                }
                return HttpResponse(json.dumps(result_error), 'application/json')

        return HttpResponse("Please, used method POST")

    @staticmethod
    def except_request(request, value):
        try:
            return request.POST[value]
        except:
            return False
