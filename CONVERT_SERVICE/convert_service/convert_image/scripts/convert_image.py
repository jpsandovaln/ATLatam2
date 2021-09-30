#
# @python_parameters.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from wand.image import Image
from wand.display import display
from wand.color import Color


class Param:
    def __init__(self, filename, grayscale, blur, adaptive_sharpen, resize, flip, flop, rotate, noise, charcoal, matrix,
                 implode, vignette):
        self.filename = filename
        self.grayscale = grayscale
        self.blur = blur
        self.adaptive_sharpen = adaptive_sharpen
        self.resize = resize
        self.flip = flip
        self.flop = flop
        self.rotate = rotate
        self.noise = noise
        self.charcoal = charcoal
        self.matrix = matrix
        self.implode = implode
        self.vignette = vignette

    def get_filename(self):
        return self.filename

    def get_grayscale(self):
        return self.grayscale

    def get_blur(self):
        return self.blur

    def get_adaptive_sharpen(self):
        return self.adaptive_sharpen

    def get_resize(self):
        return self.resize

    def get_flip(self):
        return self.flip

    def get_flop(self):
        return self.flop

    def get_rotate(self):
        return self.rotate

    def get_noise(self):
        return self.noise

    def get_charcoal(self):
        return self.charcoal

    def get_matrix(self):
        return self.matrix

    def get_implode(self):
        return self.implode

    def get_vignette(self):
        return self.vignette


class ConvertImage:

    def convert(self, param):

        # Change "IMAGE_PATH" to  image to convert
        with Image(filename='IMAGE_PATH') as img:

            img.format = 'jpg'

            if param.get_blur():
                img.blur(radius=0, sigma=6)

            if param.get_grayscale():
                img.type = 'grayscale'

            if param.get_adaptive_sharpen():
                img.adaptive_sharpen(radius=10, sigma=9)

            if param.get_resize():
                width = param.get_resize()[0]
                height = param.get_resize()[1]
                print(img.size)
                img.resize(width, height)
                print(img.size)

            if param.get_flip():
                img.flip()

            if param.get_flop():
                img.flop()

            if param.get_rotate():
                print(param.get_rotate())
                angle = param.get_rotate()[0]
                color = param.get_rotate()[1]
                img.rotate(angle, background=Color(color))

            if param.get_noise():
                img.noise("laplacian", attenuate=1.0)

            if param.get_charcoal():
                img.charcoal(radius=1.5, sigma=0.5)

            if param.get_matrix():
                matrix = [[0, 0, 1],
                          [0, 1, 0],
                          [1, 0, 0]]
                img.color_matrix(matrix)

            if param.get_implode():
                img.implode(amount=0.35)

            if param.get_vignette():
                img.vignette(sigma=3, x=10, y=10)

            img.save(filename='./results/img.jpg')

    def png_to_jpg(self):
        with Image(filename='./assets/image.png') as img:
            img.format = 'jpg'
            img.save(filename='./results/png_to_jpg/img.jpg')

    def jpg_to_png(self):
        with Image(filename='./assets/mario.jpg') as img:
            img.format = 'png'
            # img.type='grayscale'
            img.save(filename='./results/jpg_to_png/img.png')
