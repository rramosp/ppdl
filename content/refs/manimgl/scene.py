import logging
logger = logging.getLogger('matplotlib')
logger.setLevel(logging.INFO)

import os, sys

sys.path.insert(0, ".")

from manimlib import *
import manimlib as manim
from PIL import Image
from skimage.io import  imread
from manimlib.mobject.svg.drawings import *
import pyglet
pyglet.options['debug_gl'] = False

from rlxmanim.wheely import *

class Text(manim.Text):
    def __init__(self, *args, **kwargs):
        if not "color" in kwargs.keys():
            kwargs["color"] = "BLACK"
        super().__init__(*args, **kwargs)

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

def get_imagemobj(name):
    img = imread(f"imgs/{name}.png")
    img = ImageMobject(Image.fromarray(img), image_mode="RGBA")
    return img

class Wheel:

    def load(self, name):
        img = imread(f"imgs/{name}.png")
        for i in range(3):
            img[:,:,i] = 1-img[:,:,3]
        img = ImageMobject(Image.fromarray(img), image_mode="RGBA")
        return img

    def __init__(self, name="smile", size=2, pos=(0,0,0)):
        self.name = name
        self.size = size
        self.pos  = pos
        self.face = self.load(name)
        self.wheel = self.load('wheel')

        self.mgroup = Group(self.wheel, self.face)
        for mobj in self.mgroup:
            mobj.height = size
            mobj.set_x(pos[0])
            mobj.set_y(pos[1])
            mobj.set_z(pos[2])

    def rotate_wheel(self):
        return Rotate(self.wheel, np.pi)


class ImageTest1(Scene):

    def construct(self):
        f1 = Wheely(mode="scared")
        f2 = Wheely(mode="worried").move_to(Dot([0,3,0]))
        self.add(f1)
        self.add(f2)
        self.wait(2)
        self.play(Rotate(f1.wheel, np.pi))
        f1.change_mode("thinking", self)

        self.wait(2)
        self.play(ScaleInPlace(f1,0.5))
        self.play(ScaleInPlace(f2,0.5), ApplyMethod(f1.move_to, Dot([-4,0,0])))