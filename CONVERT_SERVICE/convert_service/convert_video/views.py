#
# @views.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


import os
import uuid
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.http import HttpResponse
from pathlib import Path
import json
from .model.VideoConverterModel import VideoConverterModel
from .util.Utilities import Utilities


class VideoConverter(View):
    """ Video converter endpoint """

    # Method running the video converter
    def post(self, request):
        if request.method == 'POST':

            # Generating a unique identifier as a session key
            session_key = str(uuid.uuid4().hex)

            # Get base directory for the file
            base_dir = Path(__file__).resolve().parent.parent

            try:
                # Upload files and parameters
                uploaded_file1 = request.FILES['file']
                uploaded_file2 = request.FILES['file2']
                vs_horizontally = request.POST.get('horizontally', "0")
                vs_vertically = request.POST.get('vertically', "0")
                vs_remove_audio = request.POST.get('remove_audio', "0")
                vs_rotate = request.POST.get('rotate', "0")
                vs_reduce_video = request.POST.get('reduce_video', "0")

                filename1 = session_key + "_" + uploaded_file1.name
                filename2 = session_key + "_" + uploaded_file2.name

                # Save the file
                fs = FileSystemStorage()
                fs.save(filename1, uploaded_file1)
                fs.save(filename2, uploaded_file2)

                # Set the path to the requested file
                full_filename1 = str(base_dir) + "/media/" + filename1
                full_filename2 = str(base_dir) + "/media/" + filename2

                # Call the class to convert the video
                video = VideoConverterModel()
                commands = video.GetCommandsForVideo(base_dir, session_key, vs_horizontally == "1", vs_vertically == "1",
                                                     vs_remove_audio == "1", vs_rotate == "1", vs_reduce_video == "1",
                                                     full_filename1, full_filename2)
                # Executing the commands obtained
                for cmd in commands:
                    if cmd.startswith("rename"):
                        # KB: https://pynative.com/python-rename-file/
                        os.rename(cmd.split('|')[1], cmd.split('|')[2])
                    else:
                        os.system(cmd)

                # Deleting extra files - KB: https://pynative.com/python-delete-files-and-directories/
                pattern = str(base_dir) + "/media/" + session_key + "_*"
                Utilities.delete_files_pattern(pattern)

                # Setting up the route to the final result - KB: https://try2explore.com/questions/10019689
                relative_file = Utilities.generate_final_url(request, session_key + ".mp4")

                result = {
                    "id": session_key,
                    "status": "OK",
                    "videoOutput": str(relative_file),
                    "params": {
                        "horizontally": vs_horizontally,
                        "vertically": vs_vertically,
                        "remove_audio": vs_remove_audio,
                        "rotate": vs_rotate,
                        "reduce_video": vs_reduce_video
                    }
                }
                # Result in json
                return HttpResponse(json.dumps(result), 'application/json')

            except:
                # Delete extra files - KB: https://pynative.com/python-delete-files-and-directories/
                pattern = str(base_dir) + "/media/" + session_key + "_*"
                Utilities.delete_files_pattern(pattern)

                result_error = {
                    "id": session_key,
                    "status": "error"
                }
                # Result in json
                return HttpResponse(json.dumps(result_error), 'application/json')

        return HttpResponse("Please, used method POST")
