#
# @unzip.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from zipfile import ZipFile
from zipfile import BadZipFile
from ..exceptions.zip_exception import ZipException


class Unzip:
    """Unzip file on same zip-file path"""

    # Extract the zipfile content at the same path
    @staticmethod
    def extract(path, filename):
        try:
            with ZipFile('/'.join((path, filename)), 'r') as zipObj:
                folder = zipObj.namelist()[0]
                zipObj.extractall(path)
            return '/'.join((path, folder))
        except BadZipFile as error:
            raise ZipException(error, "Please upload a valid zip file.")
