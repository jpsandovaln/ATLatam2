import glob
import os
import uuid
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.http import HttpResponse
from pathlib import Path
import json

# Create your views here.
from .model.VideoConverterModel import VideoConverterModel


class VideoConverter(View):
    def post(self, request):
        if request.method == 'POST':
            uploaded_file1 = request.FILES['file']
            uploaded_file2 = request.FILES['file2']
            par1 = request.POST.get('par1', "0")
            par2 = request.POST.get('par2', "0")
            par3 = request.POST.get('par3', "0")
            par4 = request.POST.get('par4', "0")
            par5 = request.POST.get('par5', "0")

            session_key = str(uuid.uuid4().hex)
            print(session_key + " INIT")
            try:
                filename1 = session_key + "_" + uploaded_file1.name
                filename2 = session_key + "_" + uploaded_file2.name

                fs = FileSystemStorage()
                fs.save(filename1, uploaded_file1)
                fs.save(filename2, uploaded_file2)

                base_dir = Path(__file__).resolve().parent.parent
                full_filename1 = str(base_dir) + "/media/" + filename1
                full_filename2 = str(base_dir) + "/media/" + filename2

                video = VideoConverterModel()
                commands = video.GetCommandsForVideo(base_dir, session_key, par1 == "1", par2 == "1", par3 == "1",
                                                par4 == "1", par5 == "1", full_filename1, full_filename2)

                print(session_key + " SAVED3")

                for cmd in commands:
                    print(session_key + " EXECUTING: " + cmd)
                    if cmd.startswith("rename"):
                        os.rename(cmd.split('|')[1], cmd.split('|')[2])  # KB: https://pynative.com/python-rename-file/
                    else:
                        os.system(cmd)

                # Delete extra files - KB: https://pynative.com/python-delete-files-and-directories/
                pattern = str(base_dir) + "/media/" + session_key + "_*"
                files = glob.glob(pattern)
                # deleting the files with pattern
                for file in files:
                    print(session_key + " DELETING FILE " + file)
                    os.remove(file)

                # KB: https://try2explore.com/questions/10019689
                relative_file = "http://" + str(get_current_site(request).domain) + "/media/" + session_key + ".mp4"

                result = {
                    "id": session_key,
                    "status": "OK",
                    "videoOutput": str(relative_file),
                    "params": {
                        "par1": par1,
                        "par2": par2,
                        "par3": par3,
                        "par4": par4,
                        "par5": par5
                    }
                }

                return HttpResponse(json.dumps(result), 'application/json')
            except:
                # Delete extra files - KB: https://pynative.com/python-delete-files-and-directories/
                pattern = str(base_dir) + "/media/" + session_key + "_*"
                files = glob.glob(pattern)
                # deleting the files with pattern
                for file in files:
                    print("DELETING FILE " + file)
                    # os.remove(file)

                result_error = {
                    "id": session_key,
                    "status": "error"
                }
                return HttpResponse(json.dumps(result_error), 'application/json')

        return HttpResponse("Please, used method POST")