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
import os
from zipfile import ZipFile


class Unzip:
    """Unzip file on same zip-file path"""

    # Extract the zipfile content at the same path
    @staticmethod
    def extract(path, filename):
        Unzip.validate('/'.join((path, filename)))
        with ZipFile('/'.join((path, filename)), 'r') as zipObj:
            folder = zipObj.namelist()[0]
            zipObj.extractall(path)
        return '/'.join((path, folder))

    @staticmethod
    def validate(path):
        if not os.path.isfile(path):
            raise Exception("Not valid file path to unzip")
