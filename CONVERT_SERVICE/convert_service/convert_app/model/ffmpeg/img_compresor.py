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


def compress_files(folder_path):
    folder = folder_path
    zip = zipfile.ZipFile('compress_img.zip', 'w')
    for archive in os.listdir(folder):
        if archive.endswith('.jpg'):
            zip.write(os.path.join(folder, archive))
    zip.close()

    return zip.close()
