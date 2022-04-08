import logging
import os, sys

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *


class Main(Scene):
    def construct(self):
        video_name = "joint, marginals and conditionals\nfor discrete distributions"

        play_intro_scene(self, video_name)

        self.wait(1)