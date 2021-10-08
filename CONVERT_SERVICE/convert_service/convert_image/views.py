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
from .model.Image import Image


class ImageConverter(View):
    def post(self, request):

        image = Image(request)
        param = ConvertImageParams(image.get_file_image(), request)

        try:
            new_image = ConvertImage()
            new_image.convert(param)
            # get download path
            final_path = new_image.get_final_path()
            result = {
                "status": "OK",
                "imageOutput": "http://" + str(get_current_site(request).domain) + "/" + final_path
            }
            return HttpResponse(json.dumps(result), 'application/json')
        except:
            result_error = {
                "status": "ERROR",
                "imageOutput": "NOT IMaAGE"
            }
            return HttpResponse(json.dumps(result_error), 'application/json')
        return HttpResponse("Please, used method POST")
