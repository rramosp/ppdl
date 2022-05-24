from __future__ import division
from gzip import WRITE
import logging
import os, sys
from unicodedata import decimal

from numpy import vdot

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *
import math

sys.path.insert(0, ".")


config.max_files_cached = 10000
Tex.set_default(color=BLACK)
Tex.set_default(stroke_color=BLACK)
Line.set_default(stroke_color=BLACK)
SingleStringMathTex.set_default(stroke_color=BLACK)
Text.set_default(color=BLACK,stroke_color=BLACK)


class Main(Scene):
    def construct(self):

        video_name = r"bayes theorem continuous part 02"
        play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()

        sfile = find_soundfile("bayes-theorem-04-continuous-part-02-ES")
       
        self.add_sound(sfile)

        p_z_to_s0 = MathTex(
            "P(", "z", "|", "s_{0}", "=", "22.3m", ")",
            "=",
            "{P(", "s_{0} = 22.3m", "|", "z", "\cdot", "P(z)",
            "\\over",
            "P(", "s_{0} = 22.3m", ")}", color= BLACK
        )

        p_x = MathTex(
            "P", "(", "x", ")",
            "=",
            "1",
            "\\over",
            "\\sigma \\cdot", "\\sqrt{\\euler}","2 \\pi}",
            "\euler^{-{1 //over 2} (x- \mu )^{2}/ \\sigma^{2} }"
        )




        ## credits
        self.wait(5)
        play_credits(self)

        self.wait(5)