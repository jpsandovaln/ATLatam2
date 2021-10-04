import glob
import os
from django.contrib.sites.shortcuts import get_current_site


class Utilities:
    """Utilities to generate the url of the final file and delete extra files """

    # Method that generates the url to visualize the result video
    @staticmethod
    def generate_final_url(request, namefile: str):
        relative_file = "http://" + str(get_current_site(request).domain) + "/media/" + namefile
        return relative_file

    @staticmethod
    # Method that deletes extra files - KB: https://pynative.com/python-delete-files-and-directories/
    def delete_files_pattern(pattern: str):
        files = glob.glob(pattern)
        # deleting the files with pattern
        for file in files:
            os.remove(file)
