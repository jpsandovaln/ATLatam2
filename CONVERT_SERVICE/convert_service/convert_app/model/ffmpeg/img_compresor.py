#
# @ffmpeg_execute.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import zipfile
import os
import shutil


def zip_dir(dir_path):
    new_file = dir_path + '.zip'
    # creating zip file with write mode
    zip = zipfile.ZipFile(new_file, 'w', zipfile.ZIP_DEFLATED)
    # Walk through the files in a directory
    for dir_path, dir_names, files in os.walk(dir_path):
        f_path = dir_path.replace(dir_path, '')
        f_path = f_path and f_path + os.sep
        # Writing each file into the zip
        for file in files:
            zip.write(os.path.join(dir_path, file), f_path + file)
    zip.close()

    return shutil.move(new_file, 'zip')
