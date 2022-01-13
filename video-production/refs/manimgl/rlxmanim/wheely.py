import os
import logging

import numpy as np

from manimlib import *
from manimlib.constants import *
from manimlib.mobject.svg.svg_mobject import *
from manimlib.utils.config_ops import digest_config
from skimage.io import imread

def get_imagemobj(name):
    img = imread(f"imgs/{name}.png")
    #img = ImageMobject(Image.fromarray(img), image_mode="RGBA")
    img = ImageMobject(f"imgs/{name}.png", image_mode="RGBA")
    return img


class Wheely(Group):
    CONFIG = {
        "mode": "smile"
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        super().__init__(**kwargs)
        self.wheel = get_imagemobj("wheel")
        self.face  = get_imagemobj(self.mode)
        self.add(self.wheel)
        self.add(self.face)

    def change_mode(self, mode, scene):
        new_self = self.__class__(mode)
        new_self.match_style(self)
        new_self.match_height(self)
        self.mode = mode
        scene.play(Transform(self.face, new_self.face))
        return self


class VWheely(VGroup):
    CONFIG = {
        "mode": "smile"
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        super().__init__(**kwargs)
        self.wheel = SVGMobject(file_name="imgs/wheel.svg")
        self.face  = SVGMobject(file_name=f"imgs/{mode}.svg").scale(0.4).rotate(np.pi)
        self.add(self.wheel)
        self.add(self.face)

    def change_mode(self, mode, scene):
        new_self = self.__class__(mode)
        new_self.match_style(self)
        new_self.match_height(self)
        self.mode = mode
        scene.play(Transform(self.face, new_self.face))
        return self

    
