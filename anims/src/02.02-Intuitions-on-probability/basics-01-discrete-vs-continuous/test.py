import logging
import os, sys

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *
from scipy import stats

class Main(Scene):
    def construct(self):

        self.play(Write(MathTex(r"P(x) : Domain_x \rightarrow [0,1]", r"\frac{\cdot xx }{\neg otra_cose \text{otra cosa}}", 
                                color=BLUE_E, 
                                font_size=48)
                        .move_to([0,3,0])))

        self.wait(5)
        play_credits(self)
        self.wait(5)


        return