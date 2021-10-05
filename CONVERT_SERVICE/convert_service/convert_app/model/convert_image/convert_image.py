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
import datetime

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


"""Class to convert image with many params"""
class ConvertImage:
    final_path = ''

    def get_final_path(self):
        return self.final_path

    def set_final_path(self, final_path):
        self.final_path = final_path

    def convert(self, param):

        with Image(filename=param.get_filename()) as img:

            # Blur effect
            if param.get_blur():
                blur = param.get_blur().split(",")
                blur_radius = int(blur[0])
                blur_sigma = int(blur[1])
                img.blur(radius=blur_radius, sigma=blur_sigma)

            # grayscale effect
            if param.get_grayscale():
                img.type = 'grayscale'

            # Adaptive sharpen effect
            if param.get_adaptive_sharpen():
                sharpen = param.get_adaptive_sharpen().split(",")
                sharpen_radius = int(sharpen[0])
                sharpen_sigma = int(sharpen[1])
                img.adaptive_sharpen(radius=sharpen_radius, sigma=sharpen_sigma)

            # resize image
            if param.get_resize():
                resize = param.get_resize().split(",")
                width = int(resize[0])
                height = int(resize[1])
                img.resize(width, height)

            # mirror effect horizontal
            if param.get_flip():
                img.flip()

            # mirror effect vertical
            if param.get_flop():
                img.flop()

            # rotate image
            if param.get_rotate():
                rotate = param.get_rotate().split(",")
                rotate_angle = int(rotate[0])
                rotate_color = rotate[1]
                img.rotate(rotate_angle, background=Color(rotate_color))

            # Noise effect
            if param.get_noise():
                noise_attenuate = float(param.get_noise());
                img.noise("laplacian", attenuate=noise_attenuate)

            # Charcoal effect
            if param.get_charcoal():
                charcoal = param.get_charcoal().split(",")
                charcoal_radius = int(charcoal[0])
                charcoal_sigma = int(charcoal[1])
                img.charcoal(radius=charcoal_radius, sigma=charcoal_sigma)

            # Matrix effect
            if param.get_matrix():
                matrix = [[0, 0, 1],
                          [0, 1, 0],
                          [1, 0, 0]]
                img.color_matrix(matrix)

            # Implode effect
            if param.get_implode():
                implode = float(param.get_implode())
                img.implode(amount=implode)

            # Add vignette to the image
            if param.get_vignette():
                vignette = param.get_vignette().split(",")
                vignette_sigma = int(vignette[0])
                vignette_x = int(vignette[1])
                vignette_y = int(vignette[2])
                img.vignette(sigma=vignette_sigma, x=vignette_x, y=vignette_y)

            # Generate date
            date = datetime.datetime.now()
            date = date.strftime("%Y%m%d%H%M%S")
            filename = f"media/{date}.jpg"
            final_path = f"./../convert_service/{filename}"
            self.set_final_path(filename)
            # Save image
            img.save(filename=final_path)
