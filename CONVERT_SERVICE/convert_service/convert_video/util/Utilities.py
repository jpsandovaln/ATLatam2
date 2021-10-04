import glob
import os
from django.contrib.sites.shortcuts import get_current_site


class Utilities:
    @staticmethod
    def generate_final_url(request, namefile: str):
        relative_file = "http://" + str(get_current_site(request).domain) + "/media/" + namefile
        return relative_file

    @staticmethod
    # Delete extra files - KB: https://pynative.com/python-delete-files-and-directories/
    def delete_files_pattern(pattern: str):
        files = glob.glob(pattern)
        # deleting the files with pattern
        for file in files:
            os.remove(file)
