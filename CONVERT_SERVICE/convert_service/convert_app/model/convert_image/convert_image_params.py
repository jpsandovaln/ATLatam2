class ConvertImageParams:
    """Class to manage the params to convert image"""

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
