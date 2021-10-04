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


class VideoConverterModel:
    """ Video converter """

    # Function that modifies a video in different aspects
    def GetCommandsForVideo(self,
                            BASE_DIR: str,
                            sessionkey: str,
                            vf_horizontally: bool,
                            vf_vertically: bool,
                            vf_remove_audio: bool,
                            vf_rotate: bool,
                            vf_reduce_video: bool,
                            input1,
                            input2='') -> str:

        cmd_ffmpeg = 'ffmpeg -i '

        # First output
        output = str(BASE_DIR) + "/media/" + sessionkey + '_output'
        # Final Output
        finaloutput = None

        commands = []

        # 1 Stack Videos Horizontally
        if vf_horizontally == True:
            cmd = cmd_ffmpeg + input1 + ' -i ' + input2 + ' -filter_complex hstack=inputs=2 ' + output + '.mp4'
            input1 = output + ".mp4"
            finaloutput = output
            output = output + '1'
            commands.append(cmd)

        # 2 Stack Videos Vertically
        if vf_vertically == True:
            cmd = cmd_ffmpeg + input1 + ' -i ' + input2 + ' -filter_complex vstack=inputs=2 ' + output + '.mp4'
            input1 = output + ".mp4"
            finaloutput = output
            output = output + '2'
            commands.append(cmd)

        # 3 Remove audio from a video
        if vf_remove_audio == True:
            cmd = cmd_ffmpeg + input1 + ' -c:v copy -an ' + output + '.mp4'
            entry1 = output + ".mp4"
            finaloutput = output
            output = output + '3'
            commands.append(cmd)

        # 4 Rotate the video 2 = 180 grades
            # 0 = 90 Counter clockwise and Vertical Flip (default)
            # 1 = 90 Clockwise
            # 2 = 90 CounterClockwise
            # 3 = 90 Clockwise and Vertical Flip
        if vf_rotate == True:
            cmd = cmd_ffmpeg + input1 + ' -vf "transpose=2,transpose=2" ' + output + '.mp4'
            input1 = output + ".mp4"
            finaloutput = output
            output = output + '4'
            commands.append(cmd)

        # Reduce the video to 480p
        if vf_reduce_video == True:
            cmd = cmd_ffmpeg + input + ' -vf scale=220:240 -preset slow -crf 18 ' + output + '.mp4'
            input1 = output + ".mp4"
            finaloutput = output
            output = output + '5'
            commands.append(cmd)

        # Rename the final file
        if len(commands) > 0:
            commands.append('rename|' + finaloutput.replace('\\','/') + '.mp4|' + str(BASE_DIR).replace('\\','/') + "/media/" + sessionkey + '.mp4')
        return commands

