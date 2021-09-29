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


import os

# Function that modifies a video in different aspects

def VideoConverter(par1: bool,
                   par2: bool,
                   par3: bool,
                   par4: bool,
                   par5: bool,
                   param1,
                   param2='') -> str:

    cmd1 = 'ffmpeg -i '

# 1 Stack Videos Horizontally

    if par1 == True:
        cmd = cmd1 + param1 + ' -i ' + param2 + ' -filter_complex hstack=inputs=2 ' + 'output.mp4'
        a = os.system(cmd)

# 2 Stack Videos Vertically and remove audio from a video

    if par2 == True:
        cmd = cmd1 + param1 + ' -i ' + param2 + ' -filter_complex vstack=inputs=2 ' + 'output.mp4'
        a = os.system(cmd)

# 3 Remove audio from a video

    if par3 == True:
        cmd2 = cmd1 + 'output.mp4' + ' -c:v copy -an ' + 'videosinAudio.mp4'
        a = os.system(cmd2)

# 4 Rotate the video 2 = 180 grades
    # 0 = 90 Counter clockwise and Vertical Flip (default)
    # 1 = 90 Clockwise
    # 2 = 90 CounterClockwise
    # 3 = 90 Clockwise and Vertical Flip

    if par4 == True:
        cmd = cmd1 + 'output.mp4' + ' -vf "transpose=2,transpose=2" ' + 'output2.mp4'
        a = os.system(cmd)

# Reduce the video to 480p

    if par5 == True:
        cmd = cmd1 + 'output.mp4' + ' -vf scale=220:240 -preset slow -crf 18 ' + 'output2.mp4'
        a = os.system(cmd)


VideoConverter(False, True, False, False, True, 'video_1.mp4', 'video_1.mp4')



