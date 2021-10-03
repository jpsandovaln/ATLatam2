#
# @videoConverter.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


# Function that modifies a video in different aspects

class VideoConverterModel:
    def GetCommandsForVideo(self,
                       BASE_DIR: str,
                       sessionkey: str,
                       par1: bool,
                       par2: bool,
                       par3: bool,
                       par4: bool,
                       par5: bool,
                       entrada1,
                       entrada2='') -> str:

        cmd_ffmpeg = 'ffmpeg -i '
        salida = str(BASE_DIR) + "/media/" + sessionkey + '_output'
        salidaFinal = None

        commands = []

        # 1 Stack Videos Horizontally
        if par1 == True:
            print("Ingresando par1 cmd")
            cmd = cmd_ffmpeg + entrada1 + ' -i ' + entrada2 + ' -filter_complex hstack=inputs=2 ' + salida + '.mp4'
            entrada1 = salida + ".mp4"
            salidaFinal = salida
            salida = salida + '1'
            commands.append(cmd)

        # 2 Stack Videos Vertically and remove audio from a video
        if par2 == True:
            print("Ingresando par2 cmd")
            cmd = cmd_ffmpeg + entrada1 + ' -i ' + entrada2 + ' -filter_complex vstack=inputs=2 ' + salida + '.mp4'
            entrada1 = salida + ".mp4"
            salidaFinal = salida
            salida = salida + '2'
            commands.append(cmd)

        # 3 Remove audio from a video
        if par3 == True:
            print("Ingresando par3 cmd")
            cmd = cmd_ffmpeg + entrada1 + ' -c:v copy -an ' + salida + '.mp4'
            entrada1 = salida + ".mp4"
            salidaFinal = salida
            salida = salida + '3'
            commands.append(cmd)


        # 4 Rotate the video 2 = 180 grades
            # 0 = 90 Counter clockwise and Vertical Flip (default)
            # 1 = 90 Clockwise
            # 2 = 90 CounterClockwise
            # 3 = 90 Clockwise and Vertical Flip
        if par4 == True:
            print("Ingresando par4 cmd")
            cmd = cmd_ffmpeg + entrada1 + ' -vf "transpose=2,transpose=2" ' + salida + '.mp4'
            entrada1 = salida + ".mp4"
            salidaFinal = salida
            salida = salida + '4'
            commands.append(cmd)

        # Reduce the video to 480p
        if par5 == True:
            print("Ingresando par5 cmd")
            cmd = cmd_ffmpeg + entrada1 + ' -vf scale=220:240 -preset slow -crf 18 ' + salida + '.mp4'
            entrada1 = salida + ".mp4"
            salidaFinal = salida
            salida = salida + '5'
            commands.append(cmd)

        if len(commands) > 0:
            commands.append('rename|' + salidaFinal.replace('\\','/') + '.mp4|' + str(BASE_DIR).replace('\\','/') + "/media/" + sessionkey + '.mp4')
        return commands

