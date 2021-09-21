#
# @main.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

# from frame_extractor import FrameExtractor
# from python_parameters import PythonParameters
# from folder_check import FolderCheck
# from fmex_execute import Execute

# if __name__ == '__main__':
#     # Revisamos que la carpeta images exista o la creamos
#     folderCheck = FolderCheck
#     folderCheck.execute()

#     # Pasamos los parametros
#     pythonParameters = PythonParameters('video/snek.mp4', 'images/%04d.jpg')  # Video input, Frames Output

#     # Iniciamos el extractor de frames
#     frameExtractor = FrameExtractor()

#     # Le damos los parametros y lo guardamos en la variable command
#     command = frameExtractor.build(pythonParameters)

#     # Ejecutamos nuestra clase fmex_execute
#     execute = Execute(command)
#     print(execute.run())


# En nustro output de imagenes %04d = 4 ceros equivale a 2,70 hrs, %05d = 5 ceros equivale a 27 hrs
